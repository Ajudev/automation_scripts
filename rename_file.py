import os


def rename_folder():
    for dir, subdirs, files in os.walk("."):
        for f in files:
            f_new = f.replace('DEG', 'DE')
            os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
        for sub in subdirs:
            sub_new = sub.replace('DEG', 'DE')
            os.rename(os.path.join(dir, sub), os.path.join(dir, sub_new))
    return True


if __name__ == "__main__":
    status = rename_folder()
    print(status)
