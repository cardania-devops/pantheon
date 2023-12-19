// minswap_interface.js
const { BlockFrostAPI } = require("@blockfrost/blockfrost-js");
const { BlockfrostAdapter } = require("@minswap/sdk");

// Retrieve the Blockfrost Project ID from environment variables
const blockFrostProjectId = process.env.BLOCKFROST_PROJECT_ID;

async function getCurrentPrice() {
    const api = new BlockfrostAdapter({
        blockFrost: new BlockFrostAPI({
            projectId: blockFrostProjectId,
            network: "mainnet",
        }),
    });
    // ... existing logic for fetching current price ...
}

async function getHistoricalPrices() {
    const api = new BlockfrostAdapter({
        blockFrost: new BlockFrostAPI({
            projectId: blockFrostProjectId,
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
