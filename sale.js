// Store the number of items sold
let tshirtCount = 5;
let capCount = 3;

// Store the prices
let tshirtPrice = 400;
let capPrice = 150;

// Calculate total earnings
let totalEarnings = tshirtCount * tshirtPrice + capCount * capPrice;

// Display total earnings
console.log("Total earnings: ₹" + totalEarnings);

// Change the t-shirt price
tshirtPrice = 450;

// Recalculate total earnings
let updatedTotal = tshirtCount * tshirtPrice + capCount * capPrice;

// Display updated total earnings
console.log("Updated total earnings after price change: ₹" + updatedTotal);
