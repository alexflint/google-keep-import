import gkeepapi
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("password")
    args = parser.parse_args()

    keep = gkeepapi.Keep()
    success = keep.login(args.username, args.password)

    note = keep.createNote('Todo', 'Eat breakfast')
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()


if __name__ == "__main__":
    main()
