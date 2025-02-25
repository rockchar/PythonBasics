def subreport():
    print("Report called from subpackage")


if __name__ == "__main__":
    print("This file was called directly")
else:
    print("This file was called as a module")
