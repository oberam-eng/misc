package money;

/**
 * @author Simon Dietz
 *
 */



public class Dollar extends Money {
	
	private String currency;
	
	Dollar(int amount, String currency) {
		super(amount, currency);
	}
	
	public Money times(int multiplier) {
		return Money.dollar(amount * multiplier);
	}
}
