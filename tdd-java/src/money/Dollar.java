package money;

/**
 * @author Simon Dietz
 *
 */
public class Dollar {

	int amount = 0;
	
	Dollar(int amount) {
		this.amount = amount;
	}
	
	/**
	 * @param args
	 */
	Dollar times(int multiplier) {
		return new Dollar(amount * multiplier);
	}
	
	boolean equals() {
		return true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
