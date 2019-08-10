package money;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class DollarTest {
	
	private Dollar five;
	 
	  @BeforeEach
	  void createFive() {
	    five = new Dollar(5);
	  }
	
	@ParameterizedTest(name = "times({0}) = {1}")
	@CsvSource({
		  "2, 10",
		  "3, 15"
		})
	@DisplayName("5 * 2 = 10")
	@Tag("multiplication")
	void testMultiplication(int multiplier, int expectedResult) {
		int actualResult = five.times(multiplier).amount;
		assertEquals(expectedResult, actualResult);
	}

	@Test
	@DisplayName("Equality")
	@Tag("equality")
	void testEquality() {
		assertTrue(new Dollar(5).equals(new Dollar(5)));
	}
	
}
