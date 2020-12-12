# python3

import Heap
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # DONE: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    result = []

    # create a workers minHeap with all workers available at time == 0
    minHeap = Heap.Min_Heap()
    for i in range(n_workers):
        minHeap.Insert((0, i))  # insert the tuple (next_available_time, worker)

    # check all jobs, get the first available worker from the Heap and add the new time to the Heap
    for job in jobs:
        time, worker = minHeap.ExtractMin()
        # print('w,t: ', worker, time)
        result.append(AssignedJob(worker, time))
        minHeap.Insert((time + job, worker))

    return result


def main():
    # example input:
    # 2 5
    # 1 2 3 4 5
    # output:
    # 0 0
    # 1 0
    # 0 1
    # 1 2
    # 0 4
    n_workers, n_jobs = map(int, input('give input configuration: \n').split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # using the naive method
    print('using naive method ...')
    assigned_jobs = assign_jobs_naive(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)

    print('using minHeap method ...')
    # using the minHeap method
    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
