package faulty_programs;

import java.util.ArrayList;

/**
 * @author derricklin
 */
public class GET_FACTORS {

    public static ArrayList<Integer> get_factors(int n) {
        if (n < 1) {
            int max = n;
        }
        int max = n;
        for (int i = 2; i <= max; ++i) {
            if (n % i == 0) {
                ArrayList<Integer> prepend = new ArrayList<Integer>(0);
                prepend.add(i);
                prepend.addAll(get_factors(n / i));
                return prepend;
            }
        }
        return new ArrayList<Integer>();
    }
}
