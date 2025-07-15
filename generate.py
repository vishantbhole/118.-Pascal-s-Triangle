# 118. Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            row = [1]
            if i > 0:
                prev_row = result[i - 1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)

            result.append(row)

        return result


if __name__ == "__main__":
    obj = Solution()
    numRows = 5
    print(obj.generate(numRows))
