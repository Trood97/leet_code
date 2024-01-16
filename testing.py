


#let's go again , till my brain hurts


class Solution(object):
    def maxSubArray(self, list1:list):
        n = len(list1)
        prov_arr = []
        prov_arr.append(list1[0])
        maxy = list1[0]

        for i in range(1,n):         #hedge your fence lol
            prov_arr.append(max(list1[i],list1[i]+prov_arr[i-1]))

            if prov_arr[i] > maxy:
                maxy = prov_arr[i]
        print(prov_arr)
        return maxy

ab = Solution()
print(ab.maxSubArray([1,2,3]))


