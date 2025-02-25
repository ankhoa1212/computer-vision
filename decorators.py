import cv2

"""Wraps a function that takes a frame as input and returns a window name and new frame."""


def decorator(func):
    def wrapper():
        exit_key = "q"
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()

            # pass frame to given function
            window_name, new_frame = func(frame)

            # show live feed
            cv2.imshow(f"{window_name} (press {exit_key} to exit)", new_frame)

            if cv2.waitKey(1) == ord(exit_key):
                break

        cap.release()
        cv2.destroyAllWindows()

    return wrapper
