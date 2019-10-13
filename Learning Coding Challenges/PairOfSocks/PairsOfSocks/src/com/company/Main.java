package com.company;
import java.util.*;

public class Main {

    static int sockMerchant(int n, int[] ar) {
        int count = 0;
        int value;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++){
            if (map.containsKey(ar[i])) {
                value = map.get(ar[i]);
//                value = value + 1;
                map.replace(ar[i], ++value);
            }else {
              map.put(ar[i], 1);
            }
        }
        for (Map.Entry m: map.entrySet()){
            value = (int) m.getValue();
            int pair = value / 2;
            count = count + pair;
        }
        return count;
    }
    public static void main(String[] args) {
      int[] arr = {1, 1, 1, 1, 7, 7};
      System.out.println(sockMerchant(6, arr));

    }
}
