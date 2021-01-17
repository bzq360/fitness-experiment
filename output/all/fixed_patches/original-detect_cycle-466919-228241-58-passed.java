package faulty_programs;

/**
 * @author derricklin
 */
public class DETECT_CYCLE {

    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;
        if (hare.getSuccessor() == null)
            return false;
        while (true) {
            tortoise = tortoise.getSuccessor();
            if (hare.getSuccessor() == null)
                return false;
            hare = hare.getSuccessor();
            {
                if (hare.getSuccessor() == null)
                    return false;
                tortoise = tortoise.getSuccessor();
                hare = hare.getSuccessor().getSuccessor();
                if (hare == tortoise)
                    return true;
            }
        }
    }
}
