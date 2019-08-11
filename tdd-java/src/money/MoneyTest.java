package money;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class MoneyTest {
		 
	/*
	@BeforeEach
	void createFive() {
		five = new Dollar(5)
	}
	*/
	
	@ParameterizedTest(name = "{0} times({1}) = {2}")
	@CsvSource({
		  "5, 2, 10",
		  "5, 3, 15",
		  "3, 5, 15"
		})
	@DisplayName("5 * 2 = 10")
	@Tag("math")
	void testMultiplication(int amount, int multiplier, int expectedResult) {
		Money actualDollar = Money.dollar(amount).times(multiplier);
		Money expectedDollar = Money.dollar(expectedResult);
		assertEquals(expectedDollar, actualDollar);
	}
	
	@Test
	@DisplayName("Equality")
	@Tag("equality")
	void testEquality() {
		assertTrue(Money.dollar(5).equals(Money.dollar(5)));
		assertFalse(Money.dollar(5).equals(Money.dollar(6)));
		assertTrue(Money.franc(5).equals(Money.franc(5)));
		assertFalse(Money.franc(5).equals(Money.franc(6)));
		assertFalse(Money.dollar(5).equals(Money.franc(5)));
		
	}
	
	@Test
	@DisplayName("Currency")
	@Tag("currency")
	void testCurrency() {
		assertEquals("USD", Money.dollar(1).currency());
		assertEquals("CHF", Money.franc(1).currency());
	}
	
	@Test
	@DisplayName("Franc Multiplication")
	@Tag("currency")
	void testFrancMultiplcation() {
		Money five = Money.franc(5);
		assertEquals(Money.franc(10), five.times(2));
	}
}
