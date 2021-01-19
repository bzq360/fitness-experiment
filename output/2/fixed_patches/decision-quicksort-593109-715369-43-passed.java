package faulty_programs;

import java.util.ArrayList;

/**
 * @author derricklin
 */
public class QUICKSORT {

    public static ArrayList<Integer> quicksort(ArrayList<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<Integer>();
        }
        Integer pivot = arr.get(0);
        ArrayList<Integer> lesser = new ArrayList<Integer>();
        ArrayList<Integer> greater = new ArrayList<Integer>();
        for (Integer x : arr.subList(1, arr.size())) {
            if (x <= pivot) {
                lesser.add(x);
            } else
                greater.add(x);
        }
        ArrayList<Integer> middle = new ArrayList<Integer>();
        greater = quicksort(greater);
        lesser = quicksort(lesser);
        middle.add(pivot);
        middle.addAll(greater);
        lesser.addAll(middle);
        if (arr.isEmpty()) {
            return new ArrayList<Integer>();
        }
        return lesser;
    }
}
