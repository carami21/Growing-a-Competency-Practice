#!/usr/bin/env python3
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Greet a user.")
    parser.add_argument("--name", "-n", help="Name to greet")
    args = parser.parse_args()

    name = args.name or os.getenv("USER") or "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
