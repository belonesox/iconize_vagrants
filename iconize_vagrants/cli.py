"""Console script for iconize_vagrants."""
import argparse
import sys
from .iv import main as mainn


def main():
    """Console script for iconize_vagrants."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()
    mainn()	
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
