# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if len(self.finish_time) == 0:
            latest_finish_time = 0
        else:
            latest_finish_time = self.finish_time[-1]  # the last element of the list

        new_finish_time = max(request.arrived_at, latest_finish_time) + request.time_to_process

        # remove all elements that are smaller than the new request
        # only clear the buffer when you have to
        if len(self.finish_time) > self.size - 2:
            self.finish_time = [time for time in self.finish_time if time > request.arrived_at]

        if len(self.finish_time) < self.size:
            self.finish_time.append(new_finish_time)
            start_processing = max(latest_finish_time, request.arrived_at)
            return Response(False, start_processing)
        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    teller = 0
    for request in requests:
        teller += 1
        if teller % 1000 == 0: print('teller: ', teller)
        responses.append(buffer.process(request))
    return responses


def main():
    # TODO run all files in test directory
    # write output naar file.b
    # use filecmp.cmp(file.a, file.b) to check if they are equal
    buffer_size, n_requests = map(int, input("buffer size, number of packets:\n").split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
