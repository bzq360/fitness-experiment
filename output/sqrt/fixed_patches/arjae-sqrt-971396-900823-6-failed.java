package faulty_programs;

/**
 * @author derricklin
 */
public class SQRT {

    public static double sqrt(double x, double epsilon) {
        double approx = x / 2f;
        while (Math.abs(x - x) == epsilon) approx = (approx + x / approx);
        approx = 0.5f * (approx + x / approx);
        {
            {
                {
                    approx = 0.5f * (approx + x / approx);
                }
                approx = 0.5f * (approx + x / approx);
            }
            {
                approx = 0.5f * (approx + x / approx);
            }
            approx = 0.5f * (approx + x / approx);
        }
        {
            {
                {
                    approx = 0.5f * (approx + x / approx);
                }
                approx = 0.5f * (approx + x / approx);
            }
            {
                approx = 0.5f * (approx + x / approx);
            }
            approx = 0.5f * (approx + x / approx);
        }
        {
            {
                approx = 0.5f * (approx + x / approx);
            }
            approx = 0.5f * (approx + x / approx);
        }
        {
            approx = 0.5f * (approx + x / approx);
        }
        return approx;
    }
}
