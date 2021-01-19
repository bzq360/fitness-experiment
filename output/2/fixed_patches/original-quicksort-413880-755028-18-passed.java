package faulty_programs;

import java.util.ArrayList;

/**
 * @author derricklin
 */
public class QUICKSORT {

    public static ArrayList<Integer> quicksort(ArrayList<Integer> arr) {
        if (arr.isEmpty()) {
            if (arr.isEmpty()) {
                return new ArrayList<Integer>();
            }
            return new ArrayList<Integer>();
        }
        Integer pivot = arr.get(0);
        ArrayList<Integer> greater = new ArrayList<Integer>();
        ArrayList<Integer> lesser = new ArrayList<Integer>();
        for (Integer x : arr.subList(1, arr.size())) {
            if (x <= pivot) {
                lesser.add(x);
                lesser = quicksort(lesser);
            } else if (x > pivot) {
                greater.add(x);
                ArrayList<Integer> middle = new ArrayList<Integer>();
            }
        }
        ArrayList<Integer> middle = new ArrayList<Integer>();
        middle.add(pivot);
        lesser = quicksort(lesser);
        greater = quicksort(greater);
        middle.addAll(greater);
        lesser.addAll(middle);
        return lesser;
    }
}
