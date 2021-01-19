package faulty_programs;

/**
 * @author derricklin
 */
public class DETECT_CYCLE {

    public static boolean detect_cycle(Node node) {
        Node tortoise = node;
        Node hare = node;
        while (true) {
            tortoise = tortoise.getSuccessor();
            if (hare.getSuccessor() == null)
                return false;
            hare = hare.getSuccessor();
            {
                tortoise = tortoise.getSuccessor();
                if (hare.getSuccessor() == null)
                    return false;
                hare = hare.getSuccessor().getSuccessor();
                if (hare == tortoise)
                    return true;
            }
        }
    }
}
