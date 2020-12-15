class Set:
    """"This class implements the Set structure."""

    # index 0 based, the init function creates n disjoint sets
    def __init__(self, row_counts):
        n = len(row_counts)
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)

    # implements Path Compression
    def Find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.Find(self.parents[i])
        return self.parents[i]

    # without Path Compression
    def Find_Without(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i

    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return
        if self.ranks[i_id] > self.ranks[j_id]:
            self.parents[j_id] = i_id

            self.row_counts[i_id] += self.row_counts[j_id]
            self.row_counts[j_id] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[i_id])
        else:
            self.parents[i_id] = j_id

            self.row_counts[j_id] += self.row_counts[i_id]
            self.row_counts[i_id] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[j_id])

            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1
        # self.max_row_count = max(self.row_counts)

def main():
    # example input:
    # 5 5
    # 1 1 1 1 1
    # 2 4
    # 1 3
    # 0 3
    # 4 3
    # 4 2
    # output:
    # 2 2 3 5 5

    pass
    # s = Set(6)
    # s.Union(1,3)
    # s.Union(4,1)
    # s.Union(2,0)
    # s.Union(1,2)
    # s.Union(1,5)
    # print(s.parent)
    # print(s.rank)



if __name__ == "__main__":
    main()
