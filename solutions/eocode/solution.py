"""Challenge 9"""
from typing import List


class Solution:
    """Class of challenge solution."""

    def duplicate_zeros(self, arr: List[int]):
        """Function that duplicates 0s without altering the memory used."""
        zeros = 0
        a_len = len(arr)
        secureZone = -1
        for i, v in enumerate(arr):
            if v == 0:
                secureZone = i if secureZone == -1 else secureZone
                if i + zeros + 1 < a_len:
                    zeros += 1
                else:
                    break
        b = a_len - 1
        l = b - zeros
        secureZone = secureZone + (zeros * 2)
        while l >= 0:
            if arr[l] != 0:
                arr[b] = arr[l]
                b -= 1
            else:
                if b == a_len-1 and (a_len - secureZone) % 2 == 1:
                    arr[b] = 0
                    b -= 1
                    zeros -= 1
                else:
                    arr[b] = 0
                    arr[b-1] = 0
                    b -= 2
                    zeros -= 1
            l -= 1
