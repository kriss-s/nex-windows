import win32gui

MATCH_WINDOW = 'Notepad'  # Window title
WINDOW_MOVE_TO = (0, 0, 500, 500)  # x, y, width, height
WINDOW_REPAINT = 0  # dnowhatthefuckthisdoes


def enumerate_windows(matching):
    def callback(hwnd, stack, *args):
        if hwnd and matching in win32gui.GetWindowText(hwnd):
            stack.append(hwnd)
    windows = list()
    win32gui.EnumWindows(callback, windows)
    return windows


def main():
    windows = enumerate_windows(MATCH_WINDOW)
    for window in windows:
        win32gui.MoveWindow(window, *WINDOW_MOVE_TO, WINDOW_REPAINT)
    if not windows:
        print('Found nothing matching', MATCH_WINDOW)


if __name__ == '__main__':
    main()
