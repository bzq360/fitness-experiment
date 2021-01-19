package faulty_programs;

/**
 * @author derricklin
 */
public class DETECT_CYCLE {

    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;
        while (true) {
            if (tortoise.getSuccessor() == null)
                return false;
            tortoise = tortoise.getSuccessor();
            hare.getSuccessor().getSuccessor();
            if (hare == tortoise)
                return true;
        }
    }
}
