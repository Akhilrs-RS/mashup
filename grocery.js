// Create variables for item names
let item1 = "Rice";
let item2 = "Sugar";
let item3 = "Wheat";

// Create variables for prices (per kg)
let priceRice = 60;
let priceSugar = 45;
let priceWheat = 55;

// Create variables for quantities purchased (in kg)
let qtyRice = 2;
let qtySugar = 3;
let qtyWheat = 4;

// Calculate cost for each item (price × quantity)
let costRice = priceRice * qtyRice;
let costSugar = priceSugar * qtySugar;
let costWheat = priceWheat * qtyWheat;

// Display cost for each item
console.log(item1 + " cost: ₹" + costRice);
console.log(item2 + " cost: ₹" + costSugar);
console.log(item3 + " cost: ₹" + costWheat);

// Calculate total bill
let totalBill = costRice + costSugar + costWheat;
console.log("Total bill: ₹" + totalBill);

// Change the quantity of one item (e.g., Sugar)
qtySugar = 5;

// Recalculate the total bill
costSugar = priceSugar * qtySugar;
let updatedTotal = costRice + costSugar + costWheat;

// Display the updated total bill
console.log(
  "Updated total bill after changing sugar quantity: ₹" + updatedTotal
);
