#!/bin/bash

# User Management Script

# Function to check if group exists
check_group() {
    if getent group "$1" > /dev/null 2>&1; then
        return 0  # Exists
    else
        return 1  # Does not exist
    fi
}

# Function to check if user exists
check_user() {
    if getent passwd "$1" > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Prompt for group name
while true; do
    read -p "Enter new group name: " GROUP_NAME
    if check_group "$GROUP_NAME"; then
        echo "Error: Group '$GROUP_NAME' already exists. Try another."
    else
        break
    fi
done

# Prompt for username
while true; do
    read -p "Enter new username: " USER_NAME
    if check_user "$USER_NAME"; then
        echo "Error: User '$USER_NAME' already exists. Try another."
    else
        break
    fi
done

# Create group
groupadd "$GROUP_NAME"
echo "Group '$GROUP_NAME' created successfully."

# Create user with bash shell and assign to group
useradd -m -s /bin/bash -g "$GROUP_NAME" "$USER_NAME"

# Set password for user
echo "Set password for $USER_NAME:"
passwd "$USER_NAME"

# Create directory at root with same name as user
USER_DIR="/$USER_NAME"
mkdir -p "$USER_DIR"

# Set ownership to user and group
chown "$USER_NAME:$GROUP_NAME" "$USER_DIR"

# Set permissions: owner and group full control, others none
chmod 770 "$USER_DIR"

# Set sticky bit to ensure only owner can delete their files
chmod +t "$USER_DIR"

echo "Directory '$USER_DIR' created with proper ownership and permissions."
echo "User '$USER_NAME' and group '$GROUP_NAME' setup complete."