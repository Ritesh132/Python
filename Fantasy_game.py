def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print("Total number of items:", item_total)

# Example usage
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
