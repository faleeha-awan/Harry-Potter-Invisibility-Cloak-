import cv2
import numpy as np

def capture_background():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture the background image.")
    while cap.isOpened():
        ret, background = cap.read()
        if ret:
            cv2.imshow("Background", background)
            if cv2.waitKey(1) == ord('q'):
                cv2.imwrite('image.jpg', background)
                print("Background image captured and saved as 'image.jpg'.")
                break
            elif cv2.waitKey(1) == 27:
                print("Background capture cancelled.")
                break
    cap.release()
    cv2.destroyAllWindows()

def create_invisibility_cloak():
    cap = cv2.VideoCapture(0)
    background = cv2.imread("./image.jpg")

    if background is None:
        print("Error: Background image not found. Please capture the background image first.")
        return

    while cap.isOpened():
        ret, current_frame = cap.read()
        if ret:
            HSV_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

            lower_blue_1 = np.array([90, 103, 20])
            higher_blue_1 = np.array([119, 255, 255])
            mask1 = cv2.inRange(HSV_frame, lower_blue_1, higher_blue_1)

            lower_blue_2 = np.array([180, 98, 20])
            higher_blue_2 = np.array([170, 255, 255])
            mask2 = cv2.inRange(HSV_frame, lower_blue_2, higher_blue_2)

            red_mask = mask1 + mask2

            red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 10)
            red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations = 1)

            part1 = cv2.bitwise_and(background, background, mask = red_mask)

            red_free = cv2.bitwise_not(red_mask)

            part2 = cv2.bitwise_and(current_frame, current_frame, mask = red_free)

            cv2.imshow("Invisibility Cloak", part1 + part2)

            if cv2.waitKey(5) == ord('q'):
                break
        else:
            print("Error: Unable to read frame from camera.")
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Welcome to the Invisibility Cloak Program!")
    print("Please follow the instructions carefully.")
    print("")

    while True:
        print("1. Capture Background Image")
        print("2. Create Invisibility Cloak")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            capture_background()
        elif choice == "2":
            create_invisibility_cloak()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")