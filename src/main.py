#!/usr/bin/env python3
"""极简任务队列 demo（题目背景板，别在这儿找碎片）。"""

TASKS: list[str] = []


def add(task: str) -> None:
    TASKS.append(task)


def run() -> None:
    for i, t in enumerate(TASKS, 1):
        print(f"[{i}] {t}")


if __name__ == "__main__":
    add("read the handover zip")
    run()


def clear() -> None:
    TASKS.clear()
