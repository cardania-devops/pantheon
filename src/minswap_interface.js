// minswap_interface.js
const { BlockFrostAPI } = require("@blockfrost/blockfrost-js");
const { BlockfrostAdapter } = require("@minswap/sdk");

// Retrieve the Blockfrost API key from environment variables
const blockFrostAPIKey = process.env.BLOCKFROST_API_KEY;

async function getCurrentPrice() {
    const api = new BlockfrostAdapter({
        blockFrost: new BlockFrostAPI({
            projectId: blockFrostAPIKey,
            network: "mainnet",
        }),
    });
    // ... existing logic for fetching current price ...
}

async function getHistoricalPrices() {
    const api = new BlockfrostAdapter({
        blockFrost: new BlockFrostAPI({
            projectId: blockFrostAPIKey,
            network: "mainnet",
        }),
    });
    // ... existing logic for fetching historical prices ...
}

// Execute the desired function based on command-line arguments
const action = process.argv[2];
if (action === "getCurrentPrice") {
    getCurrentPrice().then(console.log);
} else if (action === "getHistoricalPrices") {
    getHistoricalPrices().then(console.log);
}
