# python3

import Set


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        return self.parents[table]


def test_run():
    with open("./tests/02", "r") as f:
        n_tables, n_queries = map(int, f.readline().split())
        print('a: ', n_tables, n_queries)
        counts = list(map(int, f.readline().split()))
        db = Set.Set(counts)
        # print('b: ', counts)

        with open("./tests/output.txt", "w") as g:
            for i in range(n_queries):
                dst, src = map(int, f.readline().split())
                # print('c: ', dst, src)
                db.Union(dst - 1, src - 1)
                print(db.max_row_count, file=g)


def main():
    n_tables, n_queries = map(int, input('give input: \n').split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    database = Set.Set(counts)

    # test files and examples all are 1-index based; convert to 0-index base.
    for i in range(n_queries):
        dst, src = map(int, input().split())
        database.Union(dst - 1, src - 1)
        print(database.max_row_count)

    # run a file in the test directory
    test_run()


if __name__ == "__main__":
    main()
