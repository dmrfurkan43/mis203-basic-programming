### Lab Quiz - Order Approval Policy

**Test I ran:**
I tested an order of 500 TRY with 500 available stock, quantity 321, and a member customer. The order was approved and the final price was 450 TRY.

**Change after testing:**
I changed the program to reject orders when the requested quantity is greater than the available stock.

### Boundary Tests

| Order Amount | Stock | Quantity | Member | Expected Result |
| -----------: | ----: | -------: | ------ | --------------- |
|      499 TRY |   500 |      321 | yes    | No discount     |
|      500 TRY |   500 |      321 | yes    | 10% discount    |
|      501 TRY |   500 |      321 | yes    | 10% discount    |


### AI Used

AI Tool Used: OpenAI ChatGPT

I used ChatGPT to understand the task and check my Python code. I tested the program myself and made sure it worked correctly.