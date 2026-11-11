"""
Sequential Prime Counting

Count how many prime numbers exist below a specified limit.

This program performs all calculations sequentially using one
Python process. It serves as the baseline for comparing
sequential and parallel execution in HPC Fundamentals Module 4.

Usage:
    python prime-counting_serial.py
    python prime-counting_serial.py --limit 2000000

Example:
    python prime-counting_serial.py --limit 20

    Prime count: 8

No external Python packages are required.
"""

import argparse
import math
import time


def is_prime(number):
    """
    Determine whether an integer is a prime number.

    A prime number is an integer greater than 1 that is
    divisible only by 1 and itself.

    We only need to check divisors up to the square root
    of the number. If a larger divisor existed, there
    would also be a corresponding smaller divisor.

    Args:
        number (int): Number to test.

    Returns:
        bool: True if prime, otherwise False.
    """

    # Numbers less than 2 are not prime.
    if number < 2:
        return False

    # Check possible divisors from 2 through sqrt(number).
    # math.isqrt() returns the integer square root.
    for divisor in range(2, math.isqrt(number) + 1):

        # A remainder of zero means the number is divisible.
        if number % divisor == 0:
            return False

    # No divisors were found, so the number is prime.
    return True


def count_primes(start, stop):
    """
    Count prime numbers within a specified range.

    Args:
        start (int): First number to examine.
        stop (int): Upper limit (not included).

    Returns:
        int: Number of primes found in the range.
    """

    # Test every number sequentially.
    # Python treats True as 1 and False as 0 when summing.
    count = 0

    for number in range(start, stop):
        if is_prime(number):
            count += 1

    return count


def main():
    """Parse arguments, run the calculation, and report results."""

    # 1. Read command-line arguments
    parser = argparse.ArgumentParser(
        description="Count prime numbers using one Python process."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=2_000_000,
        help="Count primes below this number (default: 2000000)."
    )

    args = parser.parse_args()

    # Reject invalid limits before starting the calculation.
    if args.limit < 3:
        parser.error("--limit must be at least 3")

    # 2. Perform the sequential calculation
    # Start the timer immediately before computation.
    start_time = time.perf_counter()

    # Examine every integer from 2 up to (but not including)
    # the requested limit, using one Python process.
    total = count_primes(2, args.limit)

    # Calculate elapsed wall-clock time in seconds.
    runtime = time.perf_counter() - start_time

    # 3. Display results
    print("\nPrime Counting Calculation")
    print("--------------------------")
    print("Execution:      Sequential")
    print(f"Limit:          {args.limit:,}")
    print("Workers:        1")
    print(f"Prime count:    {total:,}")
    print(f"Runtime:        {runtime:.4f} seconds")


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()
