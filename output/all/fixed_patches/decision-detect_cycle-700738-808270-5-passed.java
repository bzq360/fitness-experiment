package faulty_programs;

/**
 * @author derricklin
 */
public class DETECT_CYCLE {

    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;
        while (true) {
            {
                {
                    if (hare.getSuccessor() == null)
                        return false;
                    tortoise = tortoise.getSuccessor();
                    hare = hare.getSuccessor().getSuccessor();
                    if (hare == tortoise)
                        return true;
                }
                if (hare == null)
                    return false;
                tortoise = tortoise.getSuccessor();
                hare = hare.getSuccessor().getSuccessor();
                if (hare == tortoise)
                    return true;
            }
            {
                if (hare.getSuccessor() == null)
                    return false;
                tortoise = tortoise.getSuccessor();
                hare = hare.getSuccessor().getSuccessor();
                if (hare == tortoise)
                    return true;
            }
            if (hare == null)
                return false;
            tortoise = tortoise.getSuccessor();
            hare = hare.getSuccessor().getSuccessor();
            if (hare == tortoise)
                return true;
        }
    }
}
