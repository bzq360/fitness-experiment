package faulty_programs;

/**
 * @author derricklin
 */
public class DETECT_CYCLE {

    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;
        while (true) {
            if (hare.getSuccessor() == null)
                return false;
            hare = hare = hare.getSuccessor();
            if (hare.getSuccessor() == tortoise)
                return true;
        }
    }
}
