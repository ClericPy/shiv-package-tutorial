import os
import platform


def main():
    pl = platform.platform()
    is_win = "windows" in pl.lower()
    with open("runtime.txt") as f:
        runtime = f.read().strip()
    suggest_runtime = "python3" if is_win else "/usr/bin/env python3"
    runtime = runtime or suggest_runtime
    cmd = (
        'shiv -o app.pyz -p "%s" -r requirements.txt --site-packages dist -e app:main'
        % runtime
    )
    line = "=" * 50
    print(
        "%s\n\nPlatform:\n%s\n\nSuggest Runtime:\n%s\n\nRunning:\n%s\n\n%s"
        % (line, pl, suggest_runtime, cmd, line)
    )
    os.system(cmd)


if __name__ == "__main__":
    main()
