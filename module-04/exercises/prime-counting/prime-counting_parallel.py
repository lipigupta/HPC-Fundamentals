"""
Parallel Prime Counting

Count how many prime numbers exist below a specified limit
using multiple Python worker processes.

Unlike the sequential version, this program divides the
number range into smaller, independent chunks. Each chunk
can be processed by a separate worker.

Python's multiprocessing.Pool manages the worker processes
and distributes the calculation among them.

Usage:
    python prime-counting_parallel.py
    python prime-counting_parallel.py --limit 2000000 --workers 4

Example:
    python prime-counting_parallel.py --limit 20 --workers 2

    Prime count: 8

This program uses multiprocessing on a single computer/node.
It does not use MPI or distribute work across multiple nodes.

No external Python packages are required.
"""

import argparse
import math
import time
from multiprocessing import Pool


def is_prime(number):
    """
    Determine whether an integer is a prime number.

    This function is identical to the sequential version.
    Parallelization changes how work is distributed, not
    how individual numbers are tested.

    Args:
        number (int): Number to test.

    Returns:
        bool: True if prime, otherwise False.
    """

    if number < 2:
        return False

    # Check possible divisors up to the integer square root.
    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return False

    return True


def count_primes(start, stop):
    """
    Count primes in the half-open interval [start, stop).

    Each worker calls this same function with a different
    portion of the overall number range.

    Args:
        start (int): First number to examine.
        stop (int): Upper limit (not included).

    Returns:
        int: Number of primes found in the assigned range.
    """

    return sum(
        is_prime(number)
        for number in range(start, stop)
    )


def main():
    """Configure workers, distribute work, and report results."""

    # 1. Read command-line arguments
    parser = argparse.ArgumentParser(
        description="Count prime numbers using multiple processes."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=2_000_000,
        help="Count primes below this number (default: 2000000)."
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=2,
        help="Number of worker processes to create (default: 2)."
    )

    args = parser.parse_args()

    # Validate inputs before creating worker processes.
    if args.limit < 3:
        parser.error("--limit must be at least 3")

    if args.workers < 1:
        parser.error("--workers must be at least 1")

    # 2. Divide the computation into independent chunks
    # Count how many integers must be tested.
    # For limit=20, we examine integers 2 through 19:
    # 20 - 2 = 18 integers.
    total_numbers = args.limit - 2

    # Calculate the number of integers per chunk.
    # Rounding up ensures that all integers are covered,
    # even when the total is not divisible by worker count.
    chunk_size = math.ceil(total_numbers / args.workers)

    # Build a list of (start, stop) tuples.
    #
    # Example: limit=20, workers=2
    #
    #   ranges = [(2, 11), (11, 20)]
    #
    # Worker 1 can examine 2 through 10.
    # Worker 2 can examine 11 through 19.
    #
    # The upper boundary is exclusive, preventing overlap.
    ranges = [
        (start, min(start + chunk_size, args.limit))
        for start in range(2, args.limit, chunk_size)
    ]

    # 3. Execute the calculation in parallel
    # Begin timing before creating the process pool.
    # This includes worker startup and task coordination.
    start_time = time.perf_counter()

    # Create a pool containing the requested number of
    # Python worker processes.
    #
    # starmap() distributes the (start, stop) tuples to
    # count_primes(), allowing different chunks to run
    # concurrently.
    #
    # The "with" statement ensures pool resources are
    # cleaned up when the calculation finishes or fails.
    with Pool(processes=args.workers) as pool:
        results = pool.starmap(count_primes, ranges)

    # 4. Combine results from all workers
    # Each worker returns a count for its assigned chunk.
    # Adding these partial counts gives the total.
    total = sum(results)

    # Stop the timer after all worker results are collected.
    runtime = time.perf_counter() - start_time


    # 5. Display results
    print("\nPrime Counting Calculation")
    print("--------------------------")
    print("Execution:      Parallel")
    print(f"Limit:          {args.limit:,}")
    print(f"Workers:        {args.workers}")
    print(f"Prime count:    {total:,}")
    print(f"Runtime:        {runtime:.4f} seconds")


# Required for safe multiprocessing startup, particularly
# on platforms that start workers using "spawn".
if __name__ == "__main__":
    main()
