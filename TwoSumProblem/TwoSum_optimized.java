package TwoSumProblem;

import java.util.HashMap;
import java.util.Map;

class TwoSum_optimized {
    public int[] twoSum(int[] InputArray, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < InputArray.length; i++) {
            if (map.containsKey(target - InputArray[i])) {
                result[1] = i;
                result[0] = map.get(target - InputArray[i]);
                return result;
            }
            map.put(InputArray[i], i);
        }
        return result;
    }

    public static void main(String[] args) {
        TwoSum_optimized one = new TwoSum_optimized();
        int[] InputArray = new int[] { 1, 2, 3, 4 };
        int[] res = one.twoSum(InputArray, 7);
        for (int i = 0; i < 2; i++) {
            System.out.println(res[i]);
        }
        System.out.println(res);

    }

}