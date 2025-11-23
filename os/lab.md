# Operating System Lab Guide

## Linux/Unix Terminal Commands

### File and Directory Operations

#### Navigation Commands
```bash
# Print working directory (shows current location)
pwd

# List files and directories
ls              # Basic listing
ls -l           # Long format (permissions, owner, size, date)
ls -a           # Show hidden files (starting with .)
ls -la          # Combined: long format + hidden files
ls -lh          # Human-readable file sizes (KB, MB, GB)
ls -lt          # Sort by modification time
ls -lS          # Sort by file size
ls -R           # Recursive listing (all subdirectories)

# Change directory
cd /path/to/directory    # Absolute path
cd relative/path         # Relative path
cd ..                    # Parent directory
cd ~                     # Home directory
cd -                     # Previous directory
```

#### File Operations
```bash
# Create files
touch filename.txt              # Create empty file or update timestamp
touch file1.txt file2.txt       # Create multiple files

# Copy files
cp source.txt destination.txt   # Copy file
cp -r dir1/ dir2/               # Copy directory recursively
cp -i file.txt dest.txt         # Interactive (prompt before overwrite)
cp -v file.txt dest.txt         # Verbose (show what's being copied)
cp -u source.txt dest.txt       # Update (copy only if source is newer)

# Move/Rename files
mv oldname.txt newname.txt      # Rename file
mv file.txt /path/to/dir/       # Move file
mv -i file.txt dest.txt         # Interactive mode
mv *.txt documents/             # Move all .txt files

# Delete files
rm filename.txt                 # Remove file
rm -i file.txt                  # Interactive (confirm before delete)
rm -f file.txt                  # Force delete (no confirmation)
rm -r directory/                # Remove directory recursively
rm -rf directory/               # Force remove directory (DANGEROUS!)

# View file contents
cat filename.txt                # Display entire file
cat file1.txt file2.txt         # Concatenate multiple files
tac filename.txt                # Display in reverse order
less filename.txt               # View file page by page (q to quit)
more filename.txt               # Similar to less (older)
head filename.txt               # First 10 lines
head -n 20 filename.txt         # First 20 lines
tail filename.txt               # Last 10 lines
tail -n 20 filename.txt         # Last 20 lines
tail -f logfile.txt             # Follow file (real-time updates)
```

#### Directory Operations
```bash
# Create directories
mkdir dirname                   # Create single directory
mkdir -p path/to/nested/dir     # Create nested directories
mkdir dir1 dir2 dir3            # Create multiple directories

# Remove directories
rmdir dirname                   # Remove empty directory
rm -r dirname                   # Remove directory and contents
rm -rf dirname                  # Force remove (DANGEROUS!)

# Directory information
du -h directory/                # Disk usage human-readable
du -sh directory/               # Summary of total size
df -h                           # Disk filesystem usage
```

### File Permissions and Ownership

```bash
# View permissions
ls -l filename.txt
# Output: -rwxr-xr-- 1 user group 1234 Nov 23 10:00 filename.txt
#         │││││││││
#         ││││││││└─ Other: read
#         │││││││└── Other: write (-)
#         ││││││└─── Other: execute (-)
#         │││││└──── Group: read
#         ││││└───── Group: write (-)
#         │││└────── Group: execute
#         ││└─────── Owner: read
#         │└──────── Owner: write
#         └───────── Owner: execute

# Change permissions
chmod 755 script.sh             # rwxr-xr-x (owner: rwx, group: r-x, others: r-x)
chmod 644 file.txt              # rw-r--r-- (owner: rw-, group: r--, others: r--)
chmod +x script.sh              # Add execute permission for all
chmod -x script.sh              # Remove execute permission
chmod u+x script.sh             # Add execute for user (owner)
chmod g+w file.txt              # Add write for group
chmod o-r file.txt              # Remove read for others
chmod -R 755 directory/         # Recursive permission change

# Permission values:
# 4 = read (r)
# 2 = write (w)
# 1 = execute (x)
# 7 = rwx (4+2+1)
# 6 = rw- (4+2)
# 5 = r-x (4+1)
# 0 = ---

# Change ownership
chown user file.txt             # Change owner
chown user:group file.txt       # Change owner and group
chown -R user directory/        # Recursive ownership change
chgrp group file.txt            # Change group only
```

### Process Management

```bash
# View processes
ps                              # Current shell processes
ps aux                          # All processes (detailed)
ps -ef                          # All processes (full format)
ps -u username                  # Processes by user
top                             # Real-time process monitor (q to quit)
htop                            # Enhanced process viewer (if installed)

# Process control
command &                       # Run in background
jobs                            # List background jobs
fg                              # Bring to foreground
fg %1                           # Bring job 1 to foreground
bg                              # Resume suspended job in background
Ctrl+Z                          # Suspend current process
Ctrl+C                          # Terminate current process

# Kill processes
kill PID                        # Terminate process (graceful)
kill -9 PID                     # Force kill
killall processname             # Kill by name
pkill pattern                   # Kill by pattern

# Process priority
nice -n 10 command              # Start with lower priority (-20 to 19)
renice -n 5 -p PID              # Change priority of running process
```

### Text Processing

```bash
# Searching in files
grep "pattern" file.txt         # Search for pattern
grep -i "pattern" file.txt      # Case-insensitive search
grep -r "pattern" directory/    # Recursive search
grep -n "pattern" file.txt      # Show line numbers
grep -v "pattern" file.txt      # Invert match (exclude pattern)
grep -c "pattern" file.txt      # Count matches
grep -l "pattern" *.txt         # List files containing pattern
grep -E "regex" file.txt        # Extended regex
egrep "pattern1|pattern2" file  # Multiple patterns

# Find files
find /path -name "filename"     # Find by name
find /path -iname "*.txt"       # Case-insensitive name search
find /path -type f              # Find files only
find /path -type d              # Find directories only
find /path -size +10M           # Files larger than 10MB
find /path -mtime -7            # Modified in last 7 days
find /path -perm 755            # Find by permission
find /path -user username       # Find by user
find /path -name "*.log" -delete # Find and delete

# Sorting and processing
sort file.txt                   # Sort lines alphabetically
sort -r file.txt                # Reverse sort
sort -n file.txt                # Numeric sort
sort -u file.txt                # Sort and remove duplicates
uniq file.txt                   # Remove adjacent duplicates
uniq -c file.txt                # Count occurrences
wc file.txt                     # Word, line, character count
wc -l file.txt                  # Line count only
wc -w file.txt                  # Word count only

# Text manipulation
cut -d',' -f1 file.csv          # Cut first field (delimiter: comma)
cut -c1-10 file.txt             # Cut characters 1-10
paste file1.txt file2.txt       # Merge lines side-by-side
tr 'a-z' 'A-Z' < file.txt       # Translate lowercase to uppercase
sed 's/old/new/' file.txt       # Replace first occurrence per line
sed 's/old/new/g' file.txt      # Replace all occurrences
sed -i 's/old/new/g' file.txt   # In-place edit
awk '{print $1}' file.txt       # Print first column
awk -F',' '{print $1,$3}' file  # Custom delimiter
```

### System Information

```bash
# System details
uname -a                        # All system information
uname -r                        # Kernel version
hostname                        # Computer name
whoami                          # Current username
id                              # User ID and groups
uptime                          # System uptime and load
date                            # Current date and time
cal                             # Calendar
lsb_release -a                  # Distribution information

# Hardware information
lscpu                           # CPU information
free -h                         # Memory usage (human-readable)
df -h                           # Disk space usage
lsblk                           # Block devices (disks)
lsusb                           # USB devices
lspci                           # PCI devices

# Network information
ifconfig                        # Network interfaces (older)
ip addr                         # IP addresses (newer)
ip link                         # Network links
netstat -tuln                   # Active network connections
ss -tuln                        # Socket statistics (newer)
ping google.com                 # Test connectivity
traceroute google.com           # Trace network path
wget URL                        # Download file
curl URL                        # Transfer data from URL
```

### Archiving and Compression

```bash
# Tar (tape archive)
tar -cvf archive.tar files/     # Create archive
tar -xvf archive.tar            # Extract archive
tar -tvf archive.tar            # List contents
tar -czvf archive.tar.gz files/ # Create compressed archive (gzip)
tar -xzvf archive.tar.gz        # Extract compressed archive
tar -cjvf archive.tar.bz2 files/# Create compressed archive (bzip2)
tar -xjvf archive.tar.bz2       # Extract bzip2 archive

# Compression tools
gzip file.txt                   # Compress (creates file.txt.gz)
gunzip file.txt.gz              # Decompress
bzip2 file.txt                  # Better compression
bunzip2 file.txt.bz2            # Decompress bzip2
zip archive.zip files           # Create ZIP archive
unzip archive.zip               # Extract ZIP archive
```

### I/O Redirection and Pipes

```bash
# Output redirection
command > file.txt              # Redirect stdout (overwrite)
command >> file.txt             # Redirect stdout (append)
command 2> error.log            # Redirect stderr
command &> all.log              # Redirect both stdout and stderr
command > /dev/null             # Discard output

# Input redirection
command < input.txt             # Use file as input

# Pipes
command1 | command2             # Pass output as input
ls -l | grep ".txt"             # List only .txt files
cat file.txt | sort | uniq      # Chain multiple commands
ps aux | grep nginx | wc -l     # Count nginx processes

# Tee (output to file and stdout)
command | tee output.txt        # Write to file and display
command | tee -a output.txt     # Append to file and display
```

### User and Group Management

```bash
# User operations
sudo command                    # Execute as superuser
sudo -i                         # Switch to root shell
su username                     # Switch user
useradd username                # Create user
passwd username                 # Change password
userdel username                # Delete user
usermod -aG group user          # Add user to group

# Group operations
groups                          # Show current user's groups
groupadd groupname              # Create group
groupdel groupname              # Delete group
```

---

## Windows Terminal Commands

### PowerShell and Command Prompt Basics

#### Navigation and File Operations
```powershell
# Navigation (PowerShell/CMD)
pwd                             # Print working directory (PowerShell)
cd                              # Print working directory (CMD)
cd C:\path\to\directory         # Change directory
cd ..                           # Parent directory
cd ~                            # Home directory (PowerShell)

# List files
dir                             # List files (CMD)
ls                              # List files (PowerShell)
Get-ChildItem                   # List files (PowerShell full)
Get-ChildItem -Force            # Include hidden files
Get-ChildItem -Recurse          # Recursive listing

# File operations
copy source.txt destination.txt # Copy file
Copy-Item source.txt dest.txt   # Copy (PowerShell)
move file.txt newlocation\      # Move file
Move-Item file.txt path\        # Move (PowerShell)
del file.txt                    # Delete file
Remove-Item file.txt            # Delete (PowerShell)
ren oldname.txt newname.txt     # Rename
type file.txt                   # Display file contents
Get-Content file.txt            # Display contents (PowerShell)

# Directory operations
mkdir dirname                   # Create directory
md dirname                      # Create directory (CMD)
rmdir dirname                   # Remove empty directory
rmdir /s dirname                # Remove directory and contents
```

#### Process Management
```powershell
# View processes
tasklist                        # List all processes
Get-Process                     # List processes (PowerShell)
Get-Process | Sort-Object CPU   # Sort by CPU usage

# Kill processes
taskkill /PID 1234              # Kill by process ID
taskkill /IM notepad.exe        # Kill by image name
Stop-Process -Name notepad      # Kill (PowerShell)
Stop-Process -Id 1234           # Kill by ID (PowerShell)
```

#### System Information
```powershell
# System details
systeminfo                      # Detailed system information
hostname                        # Computer name
whoami                          # Current user
ver                             # Windows version (CMD)
$PSVersionTable                 # PowerShell version

# Network
ipconfig                        # IP configuration
ipconfig /all                   # Detailed network info
ping google.com                 # Test connectivity
netstat -an                     # Active connections
```

---

## Vi Editor Commands

### Vi Editor Modes

Vi has three main modes:
1. **Command Mode** (default) - Navigate and execute commands
2. **Insert Mode** - Type and edit text
3. **Ex Mode** - Execute extended commands (`:`)

### Starting Vi

```bash
vi filename.txt                 # Open file (create if doesn't exist)
vi +10 filename.txt             # Open at line 10
vi +/pattern filename.txt       # Open at first match of pattern
view filename.txt               # Open in read-only mode
```

### Mode Switching

```
# From Command Mode to Insert Mode
i           # Insert before cursor
I           # Insert at beginning of line
a           # Append after cursor
A           # Append at end of line
o           # Open new line below
O           # Open new line above
R           # Replace mode (overwrite)

# From Insert/Replace Mode to Command Mode
Esc         # Return to command mode

# From Command Mode to Ex Mode  
:           # Enter ex mode command
```

### Navigation (Command Mode)

```
# Character navigation
h           # Move left
j           # Move down
k           # Move up
l           # Move right

# Word navigation
w           # Next word
b           # Previous word
e           # End of word
W           # Next word (ignore punctuation)
B           # Previous word (ignore punctuation)

# Line navigation
0           # Beginning of line
^           # First non-blank character
$           # End of line
gg          # First line of file
G           # Last line of file
:n          # Go to line n
nG          # Go to line n

# Screen navigation
H           # Top of screen
M           # Middle of screen
L           # Bottom of screen
Ctrl+f      # Page forward
Ctrl+b      # Page backward
Ctrl+d      # Half page down
Ctrl+u      # Half page up
```

### Editing (Command Mode)

```
# Deleting
x           # Delete character under cursor
X           # Delete character before cursor
dd          # Delete current line
D           # Delete from cursor to end of line
dw          # Delete word
d$          # Delete to end of line
d0          # Delete to beginning of line
dG          # Delete to end of file
dgg         # Delete to beginning of file

# Copying (yanking)
yy          # Copy current line
Y           # Copy current line
yw          # Copy word
y$          # Copy to end of line
nyy         # Copy n lines

# Pasting
p           # Paste after cursor/line
P           # Paste before cursor/line

# Undo and Redo
u           # Undo last change
Ctrl+r      # Redo
U           # Undo all changes on line

# Change
cc          # Change entire line
cw          # Change word
c$          # Change to end of line
r           # Replace single character
R           # Replace mode (overwrite)

# Join lines
J           # Join current line with next
```

### Search and Replace

```
# Searching
/pattern    # Search forward
?pattern    # Search backward
n           # Next occurrence
N           # Previous occurrence
*           # Search for word under cursor (forward)
#           # Search for word under cursor (backward)

# Find and replace
:s/old/new/         # Replace first occurrence in line
:s/old/new/g        # Replace all in line
:%s/old/new/g       # Replace all in file
:%s/old/new/gc      # Replace all with confirmation
:10,20s/old/new/g   # Replace in lines 10-20
```

### Saving and Exiting (Ex Mode)

```
:w          # Save (write)
:w filename # Save as filename
:q          # Quit (fails if unsaved changes)
:q!         # Quit without saving
:wq         # Save and quit
:x          # Save and quit (same as :wq)
ZZ          # Save and quit (command mode)
:e!         # Reload file (discard changes)
:w !sudo tee %  # Save file with sudo
```

### Advanced Features

```
# Visual mode
v           # Visual mode (character selection)
V           # Visual line mode
Ctrl+v      # Visual block mode
gv          # Reselect last visual selection

# In visual mode:
d           # Delete selection
y           # Copy selection
>           # Indent
<           # Unindent

# Marks
ma          # Set mark 'a' at current position
'a          # Jump to mark 'a'
:marks      # List all marks

# Macros
qa          # Start recording macro in register 'a'
q           # Stop recording
@a          # Execute macro 'a'
@@          # Repeat last macro

# Multiple files
:e filename     # Edit another file
:bnext or :bn   # Next buffer
:bprev or :bp   # Previous buffer
:ls             # List buffers
:b2             # Switch to buffer 2

# Windows
:split          # Horizontal split
:vsplit         # Vertical split
Ctrl+w w        # Switch windows
Ctrl+w q        # Close window
Ctrl+w o        # Close other windows
```

### Configuration

```
# .vimrc file settings
:set number         # Show line numbers
:set nonumber       # Hide line numbers
:set relativenumber # Relative line numbers
:set hlsearch       # Highlight search results
:set ignorecase     # Case-insensitive search
:set smartcase      # Smart case searching
:set autoindent     # Auto-indent new lines
:set tabstop=4      # Tab width
:set expandtab      # Use spaces instead of tabs
:syntax on          # Syntax highlighting
```

---

## Bash Scripting

### Basic Shell Script Structure

```bash
#!/bin/bash
# This is a comment
# First line is shebang - specifies interpreter

# Make script executable:
# chmod +x script.sh

# Run script:
# ./script.sh
# or
# bash script.sh
```

### Variables

```bash
#!/bin/bash

# Variable declaration (no spaces around =)
name="John"
age=25
PI=3.14159

# Using variables
echo "Name: $name"
echo "Age: $age"
echo "Age: ${age}"  # Better practice with braces

# Command substitution
current_date=$(date)
files=$(ls)
user=`whoami`  # Old style (backticks)

# Read user input
read -p "Enter your name: " username
echo "Hello, $username!"

# Read multiple values
read -p "Enter first and last name: " first last

# Read with timeout
read -t 5 -p "Enter within 5 seconds: " input

# Read password (hidden)
read -s -p "Enter password: " password

# Environment variables
echo "Home: $HOME"
echo "User: $USER"
echo "Path: $PATH"
echo "Shell: $SHELL"

# Special variables
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
echo "Exit status of last command: $?"
echo "Process ID: $$"
```

### Arithmetic Operations

```bash
#!/bin/bash

# Using let
let result=5+3
let "result = 5 + 3"
echo "Result: $result"

# Using $(( ))
result=$((5 + 3))
result=$((10 * 2))
result=$((20 / 4))
result=$((10 % 3))  # Modulo
echo "Result: $result"

# Increment/Decrement
count=5
let count++
let count--
((count++))
((count--))

# Using expr (old style)
result=$(expr 5 + 3)
result=$(expr 10 \* 2)  # Escape * in expr

# Floating point (using bc)
result=$(echo "scale=2; 10/3" | bc)
echo "Result: $result"
```

### Decision Making (if-else)

```bash
#!/bin/bash

# Basic if statement
if [ condition ]; then
    # commands
fi

# If-else
if [ condition ]; then
    # commands
else
    # commands
fi

# If-elif-else
if [ condition1 ]; then
    # commands
elif [ condition2 ]; then
    # commands
else
    # commands
fi

# Numeric comparisons
num1=10
num2=20

if [ $num1 -eq $num2 ]; then
    echo "Equal"
fi

# -eq : equal
# -ne : not equal
# -gt : greater than
# -ge : greater than or equal
# -lt : less than
# -le : less than or equal

# String comparisons
str1="hello"
str2="world"

if [ "$str1" = "$str2" ]; then
    echo "Strings are equal"
fi

if [ "$str1" != "$str2" ]; then
    echo "Strings are not equal"
fi

if [ -z "$str1" ]; then
    echo "String is empty"
fi

if [ -n "$str1" ]; then
    echo "String is not empty"
fi

# File tests
filename="test.txt"

if [ -e "$filename" ]; then
    echo "File exists"
fi

if [ -f "$filename" ]; then
    echo "Regular file"
fi

if [ -d "$filename" ]; then
    echo "Directory"
fi

if [ -r "$filename" ]; then
    echo "File is readable"
fi

if [ -w "$filename" ]; then
    echo "File is writable"
fi

if [ -x "$filename" ]; then
    echo "File is executable"
fi

if [ -s "$filename" ]; then
    echo "File is not empty"
fi

# Logical operators
if [ $num1 -gt 5 ] && [ $num2 -lt 30 ]; then
    echo "Both conditions true"
fi

if [ $num1 -gt 5 ] || [ $num2 -lt 5 ]; then
    echo "At least one condition true"
fi

if [ ! -e "$filename" ]; then
    echo "File does not exist"
fi

# Modern syntax [[ ]]
if [[ $num1 > 5 && $num2 < 30 ]]; then
    echo "Using modern syntax"
fi

if [[ $str1 == "hello" ]]; then
    echo "String match"
fi

# Pattern matching
if [[ $str1 == h* ]]; then
    echo "Starts with h"
fi
```

### Case Statement

```bash
#!/bin/bash

read -p "Enter a choice (1-3): " choice

case $choice in
    1)
        echo "You chose option 1"
        ;;
    2)
        echo "You chose option 2"
        ;;
    3)
        echo "You chose option 3"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

# Pattern matching in case
read -p "Enter a file extension: " ext

case $ext in
    txt|doc|docx)
        echo "Document file"
        ;;
    jpg|png|gif)
        echo "Image file"
        ;;
    mp3|wav|flac)
        echo "Audio file"
        ;;
    *)
        echo "Unknown file type"
        ;;
esac

# Case with ranges
read -p "Enter your grade (A-F): " grade

case $grade in
    [Aa])
        echo "Excellent!"
        ;;
    [Bb])
        echo "Good"
        ;;
    [Cc])
        echo "Average"
        ;;
    [Dd])
        echo "Below Average"
        ;;
    [Ff])
        echo "Failed"
        ;;
    *)
        echo "Invalid grade"
        ;;
esac
```

### Loop Statements

```bash
#!/bin/bash

# For loop - iterating over list
for item in apple banana cherry; do
    echo "Fruit: $item"
done

# For loop - range
for i in {1..5}; do
    echo "Number: $i"
done

# For loop - with step
for i in {0..10..2}; do
    echo "Even: $i"
done

# For loop - C-style
for ((i=1; i<=5; i++)); do
    echo "Count: $i"
done

# For loop - iterating over files
for file in *.txt; do
    echo "Processing: $file"
done

# For loop - command output
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# While loop - reading file
while read line; do
    echo "Line: $line"
done < input.txt

# While loop - infinite
while true; do
    echo "Running..."
    sleep 1
    # Use Ctrl+C to stop
done

# Until loop (opposite of while)
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Break and continue
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue  # Skip 5
    fi
    if [ $i -eq 8 ]; then
        break  # Exit loop at 8
    fi
    echo "Number: $i"
done

# Nested loops
for i in {1..3}; do
    for j in {1..3}; do
        echo "i=$i, j=$j"
    done
done
```

### String Operations

```bash
#!/bin/bash

# String length
string="Hello World"
length=${#string}
echo "Length: $length"

# Substring extraction
string="Hello World"
echo ${string:0:5}      # "Hello" (start:length)
echo ${string:6}        # "World" (from position 6)
echo ${string: -5}      # "World" (last 5 chars)

# String replacement
string="Hello World World"
echo ${string/World/Universe}    # Replace first "Hello Universe World"
echo ${string//World/Universe}   # Replace all "Hello Universe Universe"

# Remove pattern
filename="document.txt.backup"
echo ${filename%.backup}         # Remove suffix: "document.txt"
echo ${filename%.*}              # Remove extension: "document.txt"
echo ${filename%%.*}             # Remove all extensions: "document"
echo ${filename#*.}              # Remove prefix: "txt.backup"

# String concatenation
first="Hello"
second="World"
combined="$first $second"
echo "$combined"

# Convert case
string="Hello World"
echo ${string^^}        # HELLO WORLD (uppercase)
echo ${string,,}        # hello world (lowercase)
echo ${string^}         # Hello World (capitalize first)

# Check if string contains substring
string="Hello World"
if [[ $string == *"World"* ]]; then
    echo "Contains World"
fi

# String comparison
str1="hello"
str2="hello"
if [ "$str1" = "$str2" ]; then
    echo "Strings are equal"
fi

# Check if string is empty
if [ -z "$string" ]; then
    echo "String is empty"
else
    echo "String is not empty"
fi

# Default values
echo ${variable:-"default"}      # Use default if variable is unset/null
echo ${variable:="default"}      # Assign default if unset/null
echo ${variable:?"Error message"} # Error if unset/null

# Split string
IFS=',' read -ra ARRAY <<< "apple,banana,cherry"
for i in "${ARRAY[@]}"; do
    echo "$i"
done
```

### Arrays

```bash
#!/bin/bash

# Declare array
fruits=("apple" "banana" "cherry")

# Array with indices
declare -a numbers
numbers[0]=10
numbers[1]=20
numbers[2]=30

# Access elements
echo ${fruits[0]}       # First element
echo ${fruits[1]}       # Second element
echo ${fruits[@]}       # All elements
echo ${fruits[*]}       # All elements (different quoting behavior)

# Array length
echo ${#fruits[@]}      # Number of elements

# Array indices
echo ${!fruits[@]}      # All indices

# Add elements
fruits+=("date")
fruits[4]="elderberry"

# Loop through array
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# Loop with indices
for i in "${!fruits[@]}"; do
    echo "Index $i: ${fruits[$i]}"
done

# Slice array
echo ${fruits[@]:1:2}   # Elements from index 1, length 2

# Associative arrays (like dictionaries)
declare -A person
person[name]="John"
person[age]=25
person[city]="New York"

echo ${person[name]}
echo ${person[@]}       # All values
echo ${!person[@]}      # All keys

# Iterate associative array
for key in "${!person[@]}"; do
    echo "$key: ${person[$key]}"
done
```

### Functions

```bash
#!/bin/bash

# Function definition
function greet {
    echo "Hello, World!"
}

# Call function
greet

# Function with arguments
function print_name {
    echo "Name: $1"
    echo "Age: $2"
}

print_name "John" 25

# Function with return value
function add {
    local result=$(($1 + $2))
    echo $result  # Return via echo
}

sum=$(add 5 3)
echo "Sum: $sum"

# Function with return code
function check_file {
    if [ -f "$1" ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

if check_file "test.txt"; then
    echo "File exists"
else
    echo "File does not exist"
fi

# Local variables
function demo {
    local local_var="I'm local"
    global_var="I'm global"
    echo $local_var
}

demo
# echo $local_var  # Error: not accessible
echo $global_var   # Accessible

# Recursive function
function factorial {
    if [ $1 -le 1 ]; then
        echo 1
    else
        local temp=$(factorial $(($1 - 1)))
        echo $(($1 * temp))
    fi
}

result=$(factorial 5)
echo "Factorial: $result"
```

### Pipes and Redirection

```bash
#!/bin/bash

# Pipe examples
ls -l | grep ".txt"              # Filter output
cat file.txt | sort | uniq       # Chain commands
ps aux | grep nginx | awk '{print $2}' # Extract specific field

# Multiple pipes
cat /var/log/syslog | grep error | wc -l | xargs echo "Errors:"

# Named pipes (FIFO)
mkfifo mypipe
echo "Hello" > mypipe &
cat < mypipe

# Process substitution
diff <(ls dir1) <(ls dir2)       # Compare output of two commands
comm <(sort file1.txt) <(sort file2.txt)

# Here document
cat << EOF > output.txt
This is line 1
This is line 2
Variable: $HOME
EOF

# Here string
grep "pattern" <<< "string to search"

# Tee - output to file and stdout
echo "Message" | tee log.txt     # Overwrite
echo "Message" | tee -a log.txt  # Append

# Combining stdout and stderr
command > output.txt 2>&1        # Redirect both
command &> output.txt            # Shorter syntax

# Redirect stderr only
command 2> error.log

# Discard output
command > /dev/null 2>&1
```

### Practical Script Examples

#### Example 1: Menu-Based Script
```bash
#!/bin/bash

while true; do
    echo "================"
    echo "   MAIN MENU"
    echo "================"
    echo "1. Show date and time"
    echo "2. List files"
    echo "3. Show current directory"
    echo "4. Exit"
    echo "================"
    read -p "Enter choice [1-4]: " choice
    
    case $choice in
        1)
            date
            ;;
        2)
            ls -la
            ;;
        3)
            pwd
            ;;
        4)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac
    
    echo
    read -p "Press Enter to continue..."
    clear
done
```

#### Example 2: File Backup Script
```bash
#!/bin/bash

# Backup script
src_dir="$1"
backup_dir="$2"
timestamp=$(date +%Y%m%d_%H%M%S)

if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_dir> <backup_dir>"
    exit 1
fi

if [ ! -d "$src_dir" ]; then
    echo "Error: Source directory does not exist"
    exit 1
fi

mkdir -p "$backup_dir"

backup_file="$backup_dir/backup_$timestamp.tar.gz"

echo "Creating backup..."
tar -czf "$backup_file" "$src_dir"

if [ $? -eq 0 ]; then
    echo "Backup successful: $backup_file"
    echo "Backup size: $(du -h $backup_file | cut -f1)"
else
    echo "Backup failed"
    exit 1
fi
```

#### Example 3: System Monitor Script
```bash
#!/bin/bash

echo "===== System Monitor ====="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo

echo "===== Uptime ====="
uptime
echo

echo "===== CPU Usage ====="
top -bn1 | grep "Cpu(s)" | awk '{print "CPU Usage: " $2 + $4 "%"}'
echo

echo "===== Memory Usage ====="
free -h
echo

echo "===== Disk Usage ====="
df -h | grep -v tmpfs
echo

echo "===== Top 5 Processes ====="
ps aux --sort=-%cpu | head -n 6
```

#### Example 4: User Management Script
```bash
#!/bin/bash

function create_user {
    read -p "Enter username: " username
    sudo useradd -m "$username"
    sudo passwd "$username"
    echo "User $username created"
}

function delete_user {
    read -p "Enter username to delete: " username
    sudo userdel -r "$username"
    echo "User $username deleted"
}

function list_users {
    echo "System users:"
    cut -d: -f1 /etc/passwd | sort
}

case "$1" in
    create)
        create_user
        ;;
    delete)
        delete_user
        ;;
    list)
        list_users
        ;;
    *)
        echo "Usage: $0 {create|delete|list}"
        exit 1
        ;;
esac
```

#### Example 5: Log File Analyzer
```bash
#!/bin/bash

logfile="$1"

if [ ! -f "$logfile" ]; then
    echo "Error: Log file not found"
    exit 1
fi

echo "===== Log Analysis ====="
echo "Total lines: $(wc -l < $logfile)"
echo "Errors: $(grep -ic error $logfile)"
echo "Warnings: $(grep -ic warning $logfile)"
echo

echo "===== Top 10 IP Addresses ====="
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" "$logfile" | sort | uniq -c | sort -nr | head -10
echo

echo "===== Most Common Errors ====="
grep -i error "$logfile" | sort | uniq -c | sort -nr | head -5
```

---

## System Calls

### Introduction to System Calls

System calls provide an interface between a process and the operating system kernel. They allow user-level processes to request services from the kernel.

### Types of System Calls

1. **Process Control**: `fork()`, `exit()`, `wait()`, `exec()`
2. **File Management**: `open()`, `read()`, `write()`, `close()`
3. **Device Management**: `ioctl()`, `read()`, `write()`
4. **Information Maintenance**: `getpid()`, `alarm()`, `sleep()`
5. **Communication**: `pipe()`, `shmget()`, `mmap()`

### Process Control System Calls

#### fork() - Create a New Process

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    
    pid = fork();
    
    if (pid < 0) {
        // Fork failed
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child process: PID = %d\n", getpid());
        printf("Child's parent PID = %d\n", getppid());
    }
    else {
        // Parent process
        printf("Parent process: PID = %d\n", getpid());
        printf("Created child with PID = %d\n", pid);
    }
    
    return 0;
}
```

#### wait() - Wait for Child Process

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;
    
    pid = fork();
    
    if (pid == 0) {
        // Child process
        printf("Child: Executing...\n");
        sleep(2);
        printf("Child: Done\n");
        return 42;  // Exit code
    }
    else {
        // Parent process
        printf("Parent: Waiting for child...\n");
        wait(&status);
        
        if (WIFEXITED(status)) {
            printf("Parent: Child exited with code %d\n", WEXITSTATUS(status));
        }
    }
    
    return 0;
}
```

#### exec() Family - Execute a Program

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid;
    
    pid = fork();
    
    if (pid == 0) {
        // Child process - replace with new program
        printf("Child: Executing ls command\n");
        
        // Replace process image with ls
        execl("/bin/ls", "ls", "-l", NULL);
        
        // This line only executes if exec fails
        perror("exec failed");
        return 1;
    }
    else {
        // Parent process
        wait(NULL);
        printf("Parent: Child completed\n");
    }
    
    return 0;
}
```

#### exit() - Terminate Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid;
    
    pid = fork();
    
    if (pid == 0) {
        printf("Child: About to exit\n");
        exit(0);  // Normal termination
    }
    else {
        printf("Parent: Child created\n");
        wait(NULL);
        printf("Parent: Child terminated\n");
    }
    
    return 0;
}
```

### File Management System Calls

#### open(), read(), write(), close()

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char buffer[100];
    ssize_t bytes_read, bytes_written;
    
    // Open file for writing (create if doesn't exist)
    fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Write to file
    const char *text = "Hello, System Calls!\n";
    bytes_written = write(fd, text, strlen(text));
    printf("Wrote %ld bytes\n", bytes_written);
    
    // Close file
    close(fd);
    
    // Open file for reading
    fd = open("test.txt", O_RDONLY);
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Read from file
    bytes_read = read(fd, buffer, sizeof(buffer) - 1);
    buffer[bytes_read] = '\0';
    printf("Read %ld bytes: %s", bytes_read, buffer);
    
    // Close file
    close(fd);
    
    return 0;
}
```

#### lseek() - Reposition File Offset

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;
    char buffer[20];
    
    fd = open("test.txt", O_RDONLY);
    
    // Read first 10 bytes
    read(fd, buffer, 10);
    buffer[10] = '\0';
    printf("First 10 bytes: %s\n", buffer);
    
    // Move to beginning
    lseek(fd, 0, SEEK_SET);
    
    // Read again
    read(fd, buffer, 5);
    buffer[5] = '\0';
    printf("After seeking: %s\n", buffer);
    
    close(fd);
    return 0;
}
```

### Information Maintenance System Calls

#### getpid(), getppid()

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Process ID: %d\n", getpid());
    printf("Parent Process ID: %d\n", getppid());
    printf("User ID: %d\n", getuid());
    printf("Group ID: %d\n", getgid());
    
    return 0;
}
```

#### sleep(), alarm()

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>

void alarm_handler(int sig) {
    printf("Alarm triggered!\n");
}

int main() {
    // Set up signal handler
    signal(SIGALRM, alarm_handler);
    
    printf("Setting alarm for 3 seconds...\n");
    alarm(3);
    
    printf("Sleeping for 5 seconds...\n");
    sleep(5);
    
    printf("Done\n");
    return 0;
}
```

### Inter-Process Communication System Calls

#### pipe() - Create Pipe for IPC

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char buffer[100];
    
    // Create pipe
    if (pipe(pipefd) == -1) {
        perror("pipe failed");
        return 1;
    }
    
    pid = fork();
    
    if (pid == 0) {
        // Child process - read from pipe
        close(pipefd[1]);  // Close write end
        
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);
        
        close(pipefd[0]);
    }
    else {
        // Parent process - write to pipe
        close(pipefd[0]);  // Close read end
        
        const char *msg = "Message from parent";
        write(pipefd[1], msg, strlen(msg) + 1);
        
        close(pipefd[1]);
        wait(NULL);
    }
    
    return 0;
}
```

### Compiling and Running C Programs with System Calls

```bash
# Compile
gcc program.c -o program

# Run
./program

# Compile with debugging symbols
gcc -g program.c -o program

# Compile with warnings
gcc -Wall program.c -o program

# Debug with gdb
gdb ./program
```

---

## Race Conditions

### What is a Race Condition?

A race condition occurs when two or more processes/threads access shared data and try to change it simultaneously. The final result depends on the timing of execution, making the behavior unpredictable.

### Race Condition Demonstration

#### Example 1: Simple Race Condition

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int shared_counter = 0;

void increment_counter() {
    int i;
    for (i = 0; i < 100000; i++) {
        shared_counter++;  // Race condition here!
    }
}

int main() {
    pid_t pid;
    
    pid = fork();
    
    if (pid == 0) {
        // Child process
        increment_counter();
        printf("Child: counter = %d\n", shared_counter);
        exit(0);
    }
    else {
        // Parent process
        increment_counter();
        wait(NULL);
        printf("Parent: counter = %d\n", shared_counter);
    }
    
    printf("Expected: 200000, Actual: %d\n", shared_counter);
    
    return 0;
}
```

#### Example 2: Race Condition with Threads

```c
#include <stdio.h>
#include <pthread.h>

int counter = 0;

void* increment(void* arg) {
    int i;
    for (i = 0; i < 100000; i++) {
        counter++;  // Race condition!
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    
    pthread_create(&thread1, NULL, increment, NULL);
    pthread_create(&thread2, NULL, increment, NULL);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Expected: 200000, Actual: %d\n", counter);
    
    return 0;
}
```

### Solutions to Race Conditions

#### Solution 1: Using Mutex (Mutual Exclusion)

```c
#include <stdio.h>
#include <pthread.h>

int counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* increment(void* arg) {
    int i;
    for (i = 0; i < 100000; i++) {
        pthread_mutex_lock(&mutex);
        counter++;  // Critical section protected
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    
    pthread_create(&thread1, NULL, increment, NULL);
    pthread_create(&thread2, NULL, increment, NULL);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Counter: %d\n", counter);
    
    pthread_mutex_destroy(&mutex);
    
    return 0;
}
```

#### Solution 2: Using Semaphores

```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

int counter = 0;
sem_t semaphore;

void* increment(void* arg) {
    int i;
    for (i = 0; i < 100000; i++) {
        sem_wait(&semaphore);  // P operation
        counter++;
        sem_post(&semaphore);  // V operation
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    
    sem_init(&semaphore, 0, 1);  // Initialize with value 1
    
    pthread_create(&thread1, NULL, increment, NULL);
    pthread_create(&thread2, NULL, increment, NULL);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Counter: %d\n", counter);
    
    sem_destroy(&semaphore);
    
    return 0;
}
```

### Classic Synchronization Problems

#### Producer-Consumer Problem

```c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0, out = 0;

sem_t empty;  // Count of empty slots
sem_t full;   // Count of full slots
pthread_mutex_t mutex;

void* producer(void* arg) {
    int item = 0;
    while (1) {
        item++;
        
        sem_wait(&empty);  // Wait for empty slot
        pthread_mutex_lock(&mutex);
        
        // Critical section
        buffer[in] = item;
        printf("Produced: %d at position %d\n", item, in);
        in = (in + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&full);  // Signal full slot
        
        sleep(1);
    }
    return NULL;
}

void* consumer(void* arg) {
    int item;
    while (1) {
        sem_wait(&full);  // Wait for full slot
        pthread_mutex_lock(&mutex);
        
        // Critical section
        item = buffer[out];
        printf("Consumed: %d from position %d\n", item, out);
        out = (out + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);  // Signal empty slot
        
        sleep(2);
    }
    return NULL;
}

int main() {
    pthread_t prod, cons;
    
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);
    
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);
    
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);
    
    return 0;
}
```

### Compilation Instructions

```bash
# Compile program with pthread library
gcc -pthread program.c -o program

# Run
./program
```

---

## Practice Exercises

### Exercise 1: File Operations
Write a bash script that:
1. Creates a directory called "backup"
2. Copies all .txt files from current directory to backup
3. Counts and displays the number of files copied
4. Shows total size of backed up files

### Exercise 2: User Input Script
Create a script that:
1. Asks user for their name and age
2. Calculates birth year
3. Creates a file named "{name}_info.txt" with the information
4. Asks if user wants to view the file

### Exercise 3: System Monitor
Write a script that displays:
1. Current date and time
2. Number of logged-in users
3. Memory usage percentage
4. Top 5 CPU-consuming processes
5. Available disk space

### Exercise 4: Loop Practice
Create a script with a menu that allows:
1. List all files
2. Count files in directory
3. Find largest file
4. Display system uptime
5. Exit

### Exercise 5: String Manipulation
Write a script that:
1. Reads a sentence from user
2. Counts words, characters, and lines
3. Converts to uppercase
4. Reverses the string
5. Replaces spaces with underscores

### Exercise 6: File Search
Create a script that:
1. Takes a file extension as input
2. Searches for all files with that extension
3. Lists them with size and modification date
4. Asks if user wants to delete any

### Exercise 7: Process Management
Write a program that:
1. Creates a child process using fork()
2. Child executes `ls -l` command
3. Parent waits for child to complete
4. Parent displays "Child process completed"

### Exercise 8: Pipe Communication
Create a program where:
1. Parent process writes a message to pipe
2. Child process reads from pipe
3. Child converts message to uppercase
4. Child writes back to another pipe
5. Parent reads and displays result

---

## Quick Reference

### Most Common Commands
```bash
ls, cd, pwd, mkdir, rm, cp, mv, cat, grep, find, chmod, ps, top, kill
```

### File Test Operators
```bash
-e  # exists
-f  # regular file
-d  # directory
-r  # readable
-w  # writable
-x  # executable
-s  # not empty
```

### Numeric Comparison
```bash
-eq # equal
-ne # not equal
-gt # greater than
-ge # greater than or equal
-lt # less than
-le # less than or equal
```

### Special Variables
```bash
$0  # Script name
$1-$9  # Arguments
$@  # All arguments
$#  # Number of arguments
$?  # Exit status
$$  # Process ID
```

### Keyboard Shortcuts (Terminal)
```bash
Ctrl+C  # Terminate process
Ctrl+Z  # Suspend process
Ctrl+D  # EOF / Logout
Ctrl+L  # Clear screen
Ctrl+R  # Reverse search
Ctrl+A  # Beginning of line
Ctrl+E  # End of line
```

---

## Additional Resources

### Online Man Pages
```bash
man command     # Manual for any command
man ls
man grep
man bash
```

### Help Commands
```bash
command --help
command -h
info command
whatis command  # Brief description
apropos keyword # Search man pages
```

### Practice Websites
- Linux Journey (linuxjourney.com)
- OverTheWire Bandit (overthewire.org/wargames/bandit/)
- Bash Academy (bash.academy)

---
# Lab Assignment Solutions

## Decision-Making Scripts (Q1-Q5)

### Q1: Age Verification Script

**Question:** Write a Bash script that prompts the user to enter their age, and then checks if the age is greater than or equal to 18. If it is, print "You are an adult", otherwise print "You are a minor".

**Solution:**
```bash
#!/bin/bash

read -p "Enter your age: " age

if [ $age -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi
```

**Explanation:**
- `read -p` prompts the user and stores input in the `age` variable
- `-ge` means "greater than or equal to"
- The if-else structure checks the condition and prints accordingly

**Conceptual Q&A:**
**Q: What are the numeric comparison operators in bash?**
A: `-eq` (equal), `-ne` (not equal), `-gt` (greater than), `-ge` (greater than or equal), `-lt` (less than), `-le` (less than or equal)

**Q: What happens if user enters non-numeric input?**
A: The script will produce an error. To handle this, use input validation.

---

### Q2: Empty String Check

**Question:** Write a Bash script that checks if a given string is empty and prints a message accordingly.

**Solution:**
```bash
#!/bin/bash

read -p "Enter a string: " str

if [ -z "$str" ]; then
    echo "The string is empty"
else
    echo "The string is not empty"
fi
```

**Explanation:**
- `-z` tests if string length is zero (empty)
- `-n` would test if string is not empty
- Use quotes around `"$str"` to handle empty strings properly

**Conceptual Q&A:**
**Q: What's the difference between -z and -n?**
A: `-z` returns true if string is empty, `-n` returns true if string is not empty

**Q: Why use quotes around variables?**
A: Prevents word splitting and handles empty strings correctly

---

### Q3: Password Verification

**Question:** Write a Bash script that prompts the user to input a password, and then checks if the password matches a predefined value. If it does, print "Access granted", otherwise print "Access denied".

**Solution:**
```bash
#!/bin/bash

CORRECT_PASSWORD="admin123"

read -s -p "Enter password: " password
echo

if [ "$password" = "$CORRECT_PASSWORD" ]; then
    echo "Access granted"
else
    echo "Access denied"
fi
```

**Explanation:**
- `read -s` hides password input (silent mode)
- `=` compares strings for equality
- `echo` after read adds a newline after hidden input

**Conceptual Q&A:**
**Q: How to compare strings in bash?**
A: Use `=` for equality, `!=` for inequality. Use `==` in `[[ ]]` syntax.

**Q: How to make password input more secure?**
A: Use `read -s` to hide input, avoid hardcoding passwords, use encryption

---

### Q4: Even or Odd Number

**Question:** Write a Bash script that checks if a given number is even or odd and prints a message accordingly.

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

if [ $((num % 2)) -eq 0 ]; then
    echo "$num is even"
else
    echo "$num is odd"
fi
```

**Explanation:**
- `%` is the modulo operator (remainder after division)
- If `num % 2` equals 0, the number is even
- `$(( ))` is used for arithmetic operations

**Conceptual Q&A:**
**Q: What is modulo operator?**
A: Returns remainder after division. `10 % 3 = 1`, `8 % 2 = 0`

**Q: Other ways to check even/odd?**
A: Check last bit: `if [ $((num & 1)) -eq 0 ]` (bitwise AND)

---

### Q5: Positive, Negative, or Zero

**Question:** Write a Bash script that prompts the user to enter a number and checks if it is positive, negative, or zero, and prints a message accordingly.

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

if [ $num -gt 0 ]; then
    echo "$num is positive"
elif [ $num -lt 0 ]; then
    echo "$num is negative"
else
    echo "$num is zero"
fi
```

**Explanation:**
- First checks if greater than 0 (positive)
- Then checks if less than 0 (negative)
- Otherwise it must be zero
- Uses `elif` for multiple conditions

**Conceptual Q&A:**
**Q: Can we use case statement for this?**
A: Not efficiently. Case is for pattern matching, not numeric comparisons.

**Q: How to handle decimal numbers?**
A: Use `bc`: `if (( $(echo "$num > 0" | bc -l) ))`

---

## Loop Exercises (Q6-Q11)

### Q6: Print Even Numbers (1-20)

**Question:** Create a script to print all even numbers between 1 and 20 using a for/while/until loop.

**Solution 1: For Loop**
```bash
#!/bin/bash

echo "Even numbers using for loop:"
for i in {2..20..2}; do
    echo $i
done
```

**Solution 2: While Loop**
```bash
#!/bin/bash

echo "Even numbers using while loop:"
i=2
while [ $i -le 20 ]; do
    echo $i
    i=$((i + 2))
done
```

**Solution 3: Until Loop**
```bash
#!/bin/bash

echo "Even numbers using until loop:"
i=2
until [ $i -gt 20 ]; do
    echo $i
    i=$((i + 2))
done
```

**Explanation:**
- For loop: `{2..20..2}` means start at 2, end at 20, step by 2
- While loop: continues while condition is true
- Until loop: continues until condition becomes true

**Conceptual Q&A:**
**Q: Difference between while and until?**
A: While runs when condition is true, until runs when condition is false.

**Q: Which loop is most efficient?**
A: For loops with ranges are generally fastest for fixed iterations.

---

### Q7: Multiplication Table of 5

**Question:** Use a for/while/until loop to print the multiplication table of 5.

**Solution 1: For Loop**
```bash
#!/bin/bash

echo "Multiplication table of 5 (for loop):"
for i in {1..10}; do
    result=$((5 * i))
    echo "5 x $i = $result"
done
```

**Solution 2: While Loop**
```bash
#!/bin/bash

echo "Multiplication table of 5 (while loop):"
i=1
while [ $i -le 10 ]; do
    result=$((5 * i))
    echo "5 x $i = $result"
    i=$((i + 1))
done
```

**Solution 3: Until Loop**
```bash
#!/bin/bash

echo "Multiplication table of 5 (until loop):"
i=1
until [ $i -gt 10 ]; do
    result=$((5 * i))
    echo "5 x $i = $result"
    i=$((i + 1))
done
```

**Conceptual Q&A:**
**Q: How to make it accept any number as input?**
A: Replace 5 with a variable: `read -p "Enter number: " num`

---

### Q8: Reverse a Number

**Question:** Write a while/for/until loop to reverse and print a given number (e.g., 1234 → 4321).

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

original=$num
reverse=0

while [ $num -gt 0 ]; do
    digit=$((num % 10))          # Extract last digit
    reverse=$((reverse * 10 + digit))  # Build reversed number
    num=$((num / 10))            # Remove last digit
done

echo "Original: $original"
echo "Reversed: $reverse"
```

**Explanation:**
- Extract last digit using modulo (`num % 10`)
- Build reversed number by multiplying by 10 and adding digit
- Remove last digit using integer division (`num / 10`)

**Conceptual Q&A:**
**Q: How does the algorithm work?**
A: For 1234: Extract 4, reverse=4. Extract 3, reverse=43. Extract 2, reverse=432. Extract 1, reverse=4321.

**Q: How to reverse without arithmetic?**
A: Use string manipulation: `echo $num | rev`

---

### Q9: Print Patterns

**Question:** Print all the below patterns using for/while/until loop.

**Pattern 1: Right Triangle**
```
*
**
***
****
*****
```

**Solution:**
```bash
#!/bin/bash

for i in {1..5}; do
    for j in $(seq 1 $i); do
        echo -n "*"
    done
    echo
done
```

**Pattern 2: Inverted Triangle**
```
*****
****
***
**
*
```

**Solution:**
```bash
#!/bin/bash

for i in {5..1}; do
    for j in $(seq 1 $i); do
        echo -n "*"
    done
    echo
done
```

**Pattern 3: Pyramid**
```
    *
   ***
  *****
 *******
*********
```

**Solution:**
```bash
#!/bin/bash

n=5
for i in $(seq 1 $n); do
    # Print spaces
    for j in $(seq 1 $((n - i))); do
        echo -n " "
    done
    # Print stars
    for k in $(seq 1 $((2 * i - 1))); do
        echo -n "*"
    done
    echo
done
```

**Pattern 4: Number Pattern**
```
1
12
123
1234
12345
```

**Solution:**
```bash
#!/bin/bash

for i in {1..5}; do
    for j in $(seq 1 $i); do
        echo -n "$j"
    done
    echo
done
```

**Conceptual Q&A:**
**Q: What does echo -n do?**
A: Prints without newline, allowing multiple prints on same line.

**Q: How to make pattern size dynamic?**
A: Use `read -p "Enter size: " n` and use `$n` instead of fixed value.

---

### Q10: Pass/Fail Based on Marks

**Question:** Create a script to print "Pass" for marks ≥ 50 and "Fail" otherwise using a for/while/until loop.

**Solution:**
```bash
#!/bin/bash

# Array of marks
marks=(45 78 32 90 55 48 67 23 81 95)

echo "Results:"
for mark in "${marks[@]}"; do
    if [ $mark -ge 50 ]; then
        echo "Marks: $mark - Pass"
    else
        echo "Marks: $mark - Fail"
    fi
done
```

**Alternative with User Input:**
```bash
#!/bin/bash

read -p "How many students? " n

for ((i=1; i<=n; i++)); do
    read -p "Enter marks for student $i: " marks
    
    if [ $marks -ge 50 ]; then
        echo "Student $i: Pass"
    else
        echo "Student $i: Fail"
    fi
done
```

**Conceptual Q&A:**
**Q: How to count total pass/fail?**
A: Initialize counters: `pass=0; fail=0` and increment in conditions.

---

### Q11: Print 1-100, Skip Multiples of 3

**Question:** Use all three loops to print numbers 1–100 but skip multiples of 3.

**Solution 1: For Loop**
```bash
#!/bin/bash

echo "Using for loop:"
for i in {1..100}; do
    if [ $((i % 3)) -ne 0 ]; then
        echo $i
    fi
done
```

**Solution 2: While Loop**
```bash
#!/bin/bash

echo "Using while loop:"
i=1
while [ $i -le 100 ]; do
    if [ $((i % 3)) -ne 0 ]; then
        echo $i
    fi
    i=$((i + 1))
done
```

**Solution 3: Until Loop**
```bash
#!/bin/bash

echo "Using until loop:"
i=1
until [ $i -gt 100 ]; do
    if [ $((i % 3)) -ne 0 ]; then
        echo $i
    fi
    i=$((i + 1))
done
```

**Using Continue:**
```bash
#!/bin/bash

for i in {1..100}; do
    if [ $((i % 3)) -eq 0 ]; then
        continue  # Skip multiples of 3
    fi
    echo $i
done
```

**Conceptual Q&A:**
**Q: Difference between continue and break?**
A: `continue` skips to next iteration, `break` exits the loop entirely.

---

## Number Theory Problems (Q12-Q16)

### Q12: Perfect Number

**Question:** Write a shell script to check whether a given number is a Perfect Number or not. (A perfect number is equal to the sum of its proper divisors — e.g., 6 = 1 + 2 + 3)

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

sum=0

# Find divisors and calculate sum
for ((i=1; i<num; i++)); do
    if [ $((num % i)) -eq 0 ]; then
        sum=$((sum + i))
    fi
done

if [ $sum -eq $num ]; then
    echo "$num is a Perfect Number"
else
    echo "$num is not a Perfect Number (sum of divisors = $sum)"
fi
```

**Explanation:**
- Perfect number equals sum of its proper divisors (excluding itself)
- Loop from 1 to num-1, check if each is a divisor
- If `num % i == 0`, then i is a divisor
- Examples: 6 (1+2+3), 28 (1+2+4+7+14), 496

**Conceptual Q&A:**
**Q: What are the first few perfect numbers?**
A: 6, 28, 496, 8128, 33550336

**Q: How to optimize the algorithm?**
A: Only loop till √num, add both i and num/i as divisors.

---

### Q13: Armstrong Number

**Question:** Write a script to check whether a given number is an Armstrong Number. (Armstrong number = sum of cubes of its digits — e.g., 153 = 1³ + 5³ + 3³)

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

original=$num
sum=0
digits=0

# Count digits
temp=$num
while [ $temp -gt 0 ]; do
    digits=$((digits + 1))
    temp=$((temp / 10))
done

# Calculate sum of digits raised to power of digit count
temp=$num
while [ $temp -gt 0 ]; do
    digit=$((temp % 10))
    
    # Calculate digit^digits
    power=1
    for ((i=1; i<=digits; i++)); do
        power=$((power * digit))
    done
    
    sum=$((sum + power))
    temp=$((temp / 10))
done

if [ $sum -eq $original ]; then
    echo "$original is an Armstrong Number"
else
    echo "$original is not an Armstrong Number (sum = $sum)"
fi
```

**Explanation:**
- Armstrong number: sum of digits raised to power of number of digits
- First count total digits
- Then extract each digit, raise to power, sum them
- Examples: 153 (1³+5³+3³=153), 9474 (9⁴+4⁴+7⁴+4⁴=9474)

**Conceptual Q&A:**
**Q: What are some Armstrong numbers?**
A: Single digit: 1-9. Three digit: 153, 370, 371, 407. Four digit: 1634, 8208, 9474

---

### Q14: Fibonacci Series

**Question:** Write a shell script to print the Fibonacci series up to n terms. (Output → 0 1 1 2 3 5 8...)

**Solution:**
```bash
#!/bin/bash

read -p "Enter number of terms: " n

a=0
b=1

echo "Fibonacci series:"
echo -n "$a "

if [ $n -gt 1 ]; then
    echo -n "$b "
fi

for ((i=3; i<=n; i++)); do
    c=$((a + b))
    echo -n "$c "
    a=$b
    b=$c
done

echo
```

**Explanation:**
- Fibonacci: Each number is sum of previous two
- Start with 0, 1
- Next = previous + previous to previous
- Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

**Conceptual Q&A:**
**Q: What's the formula for nth Fibonacci number?**
A: Binet's formula: Fn = (φⁿ - ψⁿ) / √5, where φ = (1+√5)/2

**Q: Where is Fibonacci used?**
A: Nature (flower petals, spirals), algorithms (dynamic programming), finance

---

### Q15: Palindrome Number

**Question:** Write a script to check whether a given number is a Palindrome (same forward and backward).

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

original=$num
reverse=0

# Reverse the number
while [ $num -gt 0 ]; do
    digit=$((num % 10))
    reverse=$((reverse * 10 + digit))
    num=$((num / 10))
done

if [ $reverse -eq $original ]; then
    echo "$original is a Palindrome"
else
    echo "$original is not a Palindrome (reversed: $reverse)"
fi
```

**Explanation:**
- Palindrome reads same forwards and backwards
- Reverse the number using loop
- Compare with original
- Examples: 121, 1331, 12321

**Conceptual Q&A:**
**Q: How to check string palindrome?**
A: Reverse string and compare: `rev_str=$(echo $str | rev)`

---

### Q16: Prime Number

**Question:** Write a shell script to check if a given number is Prime or not.

**Solution:**
```bash
#!/bin/bash

read -p "Enter a number: " num

# Handle special cases
if [ $num -lt 2 ]; then
    echo "$num is not a Prime number"
    exit 0
fi

if [ $num -eq 2 ]; then
    echo "$num is a Prime number"
    exit 0
fi

# Check if divisible by any number from 2 to sqrt(num)
is_prime=1
for ((i=2; i*i<=num; i++)); do
    if [ $((num % i)) -eq 0 ]; then
        is_prime=0
        break
    fi
done

if [ $is_prime -eq 1 ]; then
    echo "$num is a Prime number"
else
    echo "$num is not a Prime number"
fi
```

**Explanation:**
- Prime: number divisible only by 1 and itself
- Numbers < 2 are not prime
- Only need to check divisors up to √num
- If any divisor found, not prime

**Conceptual Q&A:**
**Q: Why check only till √num?**
A: If num has a divisor > √num, it must have one < √num too.

**Q: How to find all primes up to N?**
A: Use Sieve of Eratosthenes algorithm.

---

## Function Implementations (Q17-Q20)

### Q17: Calculator Function

**Question:** Write a function calculate() that takes two numbers and an operator (+, -, *, /) as arguments and performs the corresponding arithmetic operation.

**Solution:**
```bash
#!/bin/bash

calculate() {
    local num1=$1
    local num2=$2
    local operator=$3
    local result
    
    case $operator in
        +)
            result=$((num1 + num2))
            ;;
        -)
            result=$((num1 - num2))
            ;;
        \*)
            result=$((num1 * num2))
            ;;
        /)
            if [ $num2 -eq 0 ]; then
                echo "Error: Division by zero"
                return 1
            fi
            result=$((num1 / num2))
            ;;
        *)
            echo "Error: Invalid operator"
            return 1
            ;;
    esac
    
    echo "$num1 $operator $num2 = $result"
}

# Test the function
read -p "Enter first number: " n1
read -p "Enter second number: " n2
read -p "Enter operator (+, -, *, /): " op

calculate $n1 $n2 "$op"
```

**Conceptual Q&A:**
**Q: Why use local variables in functions?**
A: Prevent variable name conflicts and side effects outside function.

**Q: How to handle floating point?**
A: Use `bc`: `result=$(echo "scale=2; $num1 / $num2" | bc)`

---

### Q18: Reverse String Function

**Question:** Write a function reverse_string() that takes a string as input and prints its reverse. Do not use external commands like rev.

**Solution:**
```bash
#!/bin/bash

reverse_string() {
    local str="$1"
    local length=${#str}
    local reversed=""
    
    for ((i=length-1; i>=0; i--)); do
        reversed="${reversed}${str:i:1}"
    done
    
    echo "$reversed"
}

# Test the function
read -p "Enter a string: " input
result=$(reverse_string "$input")
echo "Original: $input"
echo "Reversed: $result"
```

**Explanation:**
- `${#str}` gets string length
- `${str:i:1}` extracts character at position i
- Loop from end to beginning, building reversed string

**Conceptual Q&A:**
**Q: How to reverse word by word?**
A: Split into array and reverse array order.

---

### Q19: Count Vowels Function

**Question:** Write a function count_vowels() that takes a string as input and prints the total number of vowels present in it.

**Solution:**
```bash
#!/bin/bash

count_vowels() {
    local str="$1"
    local count=0
    local length=${#str}
    
    # Convert to lowercase for easier checking
    str=$(echo "$str" | tr '[:upper:]' '[:lower:]')
    
    for ((i=0; i<length; i++)); do
        char="${str:i:1}"
        case $char in
            a|e|i|o|u)
                count=$((count + 1))
                ;;
        esac
    done
    
    echo $count
}

# Test the function
read -p "Enter a string: " input
vowels=$(count_vowels "$input")
echo "Number of vowels: $vowels"
```

**Explanation:**
- Convert to lowercase for uniform checking
- Extract each character
- Use case to match against vowels
- Increment counter for each match

**Conceptual Q&A:**
**Q: How to count each vowel separately?**
A: Use separate counters for a, e, i, o, u.

---

### Q20: Second Largest Number

**Question:** Write a function 2nd_largest() that accepts three numbers as arguments and prints the second largest among them using if conditions.

**Solution:**
```bash
#!/bin/bash

second_largest() {
    local a=$1
    local b=$2
    local c=$3
    local second
    
    if [ $a -ge $b ] && [ $a -ge $c ]; then
        # a is largest
        if [ $b -ge $c ]; then
            second=$b
        else
            second=$c
        fi
    elif [ $b -ge $a ] && [ $b -ge $c ]; then
        # b is largest
        if [ $a -ge $c ]; then
            second=$a
        else
            second=$c
        fi
    else
        # c is largest
        if [ $a -ge $b ]; then
            second=$a
        else
            second=$b
        fi
    fi
    
    echo "Second largest: $second"
}

# Test the function
read -p "Enter first number: " n1
read -p "Enter second number: " n2
read -p "Enter third number: " n3

second_largest $n1 $n2 $n3
```

**Alternative Using Sorting:**
```bash
#!/bin/bash

second_largest() {
    local nums=($1 $2 $3)
    
    # Bubble sort
    for ((i=0; i<3; i++)); do
        for ((j=0; j<2-i; j++)); do
            if [ ${nums[j]} -gt ${nums[j+1]} ]; then
                temp=${nums[j]}
                nums[j]=${nums[j+1]}
                nums[j+1]=$temp
            fi
        done
    done
    
    echo "Second largest: ${nums[1]}"
}
```

**Conceptual Q&A:**
**Q: How to find second largest in array of n elements?**
A: Sort and take second last, or track largest and second largest in single pass.

## String and Array Operations (Q21-Q24)

### Q21: Count Vowels, Consonants, Digits, and Spaces

**Question:** Write a shell script to count vowels, consonants, digits, and spaces in a given string.

**Solution:**
```bash
#!/bin/bash

read -p "Enter a string: " str

vowels=0
consonants=0
digits=0
spaces=0
special=0

length=${#str}

for ((i=0; i<length; i++)); do
    char="${str:i:1}"
    
    case $char in
        [aeiouAEIOU])
            vowels=$((vowels + 1))
            ;;
        [a-zA-Z])
            consonants=$((consonants + 1))
            ;;
        [0-9])
            digits=$((digits + 1))
            ;;
        " ")
            spaces=$((spaces + 1))
            ;;
        *)
            special=$((special + 1))
            ;;
    esac
done

echo "Vowels: $vowels"
echo "Consonants: $consonants"
echo "Digits: $digits"
echo "Spaces: $spaces"
echo "Special characters: $special"
```

**Conceptual Q&A:**
**Q: How does case pattern matching work?**
A: `[aeiou]` matches any single character in the set. `[a-z]` matches range.

---

### Q22: Reverse String and Check Palindrome

**Question:** Write a shell script to reverse a given string and check whether it is a palindrome (using user-defined function).

**Solution:**
```bash
#!/bin/bash

reverse_string() {
    local str="$1"
    local length=${#str}
    local reversed=""
    
    for ((i=length-1; i>=0; i--)); do
        reversed="${reversed}${str:i:1}"
    done
    
    echo "$reversed"
}

is_palindrome() {
    local str="$1"
    local reversed=$(reverse_string "$str")
    
    if [ "$str" = "$reversed" ]; then
        return 0  # True
    else
        return 1  # False
    fi
}

# Main program
read -p "Enter a string: " input

reversed=$(reverse_string "$input")
echo "Original: $input"
echo "Reversed: $reversed"

if is_palindrome "$input"; then
    echo "The string is a palindrome"
else
    echo "The string is not a palindrome"
fi
```

**Conceptual Q&A:**
**Q: What does return 0 mean in bash?**
A: Return 0 indicates success/true, non-zero indicates failure/false.

---

### Q23: Find Maximum in Array

**Question:** Write a function find_max() that accepts an array of integers and returns the maximum value.

**Solution:**
```bash
#!/bin/bash

find_max() {
    local arr=("$@")  # Accept all arguments as array
    local max=${arr[0]}
    
    for num in "${arr[@]}"; do
        if [ $num -gt $max ]; then
            max=$num
        fi
    done
    
    echo $max
}

# Test the function
echo "Enter numbers separated by spaces:"
read -a numbers

maximum=$(find_max "${numbers[@]}")
echo "Maximum value: $maximum"
```

**Alternative - More Robust:**
```bash
#!/bin/bash

find_max() {
    local arr=("$@")
    local max=${arr[0]}
    local length=${#arr[@]}
    
    if [ $length -eq 0 ]; then
        echo "Error: Empty array"
        return 1
    fi
    
    for ((i=1; i<length; i++)); do
        if [ ${arr[i]} -gt $max ]; then
            max=${arr[i]}
        fi
    done
    
    echo $max
}

# Define array
numbers=(23 67 12 89 45 34 91 56)
echo "Array: ${numbers[@]}"
max=$(find_max "${numbers[@]}")
echo "Maximum: $max"
```

**Conceptual Q&A:**
**Q: How to find both min and max?**
A: Track both in same loop, return as string or use global variables.

---

### Q24: Sort Array (Bubble Sort)

**Question:** Write a function sort_array() that sorts an array of integers in ascending order using simple sorting logic (no external commands like sort).

**Solution:**
```bash
#!/bin/bash

sort_array() {
    local arr=("$@")
    local n=${#arr[@]}
    
    # Bubble sort
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n-i-1; j++)); do
            if [ ${arr[j]} -gt ${arr[j+1]} ]; then
                # Swap
                temp=${arr[j]}
                arr[j]=${arr[j+1]}
                arr[j+1]=$temp
            fi
        done
    done
    
    echo "${arr[@]}"
}

# Test the function
numbers=(64 34 25 12 22 11 90)
echo "Original array: ${numbers[@]}"

sorted=($(sort_array "${numbers[@]}"))
echo "Sorted array: ${sorted[@]}"
```

**Selection Sort Alternative:**
```bash
#!/bin/bash

selection_sort() {
    local arr=("$@")
    local n=${#arr[@]}
    
    for ((i=0; i<n-1; i++)); do
        min_idx=$i
        
        # Find minimum element
        for ((j=i+1; j<n; j++)); do
            if [ ${arr[j]} -lt ${arr[min_idx]} ]; then
                min_idx=$j
            fi
        done
        
        # Swap with first unsorted element
        if [ $min_idx -ne $i ]; then
            temp=${arr[i]}
            arr[i]=${arr[min_idx]}
            arr[min_idx]=$temp
        fi
    done
    
    echo "${arr[@]}"
}
```

**Conceptual Q&A:**
**Q: Time complexity of bubble sort?**
A: O(n²) in worst and average case, O(n) best case (already sorted).

**Q: Which sorting algorithm is best for small arrays?**
A: Insertion sort for very small arrays, selection sort is also simple.

---

## Matrix Operations (Q25-Q30)

### Q25: Matrix Addition/Subtraction/Multiplication

**Question:** Write a shell script to perform addition/subtraction/multiplication of 3×3 matrix.

**Solution:**
```bash
#!/bin/bash

# Read matrix
read_matrix() {
    local name=$1
    local -n matrix=$2
    
    echo "Enter $name matrix (3x3):"
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local -n matrix=$1
    
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3; j++)); do
            echo -n "${matrix[$i,$j]} "
        done
        echo
    done
}

# Matrix addition
matrix_add() {
    local -n mat1=$1
    local -n mat2=$2
    local -n result=$3
    
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3; j++)); do
            result[$i,$j]=$((mat1[$i,$j] + mat2[$i,$j]))
        done
    done
}

# Matrix subtraction
matrix_sub() {
    local -n mat1=$1
    local -n mat2=$2
    local -n result=$3
    
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3; j++)); do
            result[$i,$j]=$((mat1[$i,$j] - mat2[$i,$j]))
        done
    done
}

# Matrix multiplication
matrix_mul() {
    local -n mat1=$1
    local -n mat2=$2
    local -n result=$3
    
    for ((i=0; i<3; i++)); do
        for ((j=0; j<3; j++)); do
            result[$i,$j]=0
            for ((k=0; k<3; k++)); do
                result[$i,$j]=$((result[$i,$j] + mat1[$i,$k] * mat2[$k,$j]))
            done
        done
    done
}

# Main program
declare -A mat_a mat_b mat_result

read_matrix "first" mat_a
read_matrix "second" mat_b

echo -e "\nFirst Matrix:"
display_matrix mat_a

echo -e "\nSecond Matrix:"
display_matrix mat_b

# Perform operations
echo -e "\n--- ADDITION ---"
matrix_add mat_a mat_b mat_result
display_matrix mat_result

echo -e "\n--- SUBTRACTION ---"
matrix_sub mat_a mat_b mat_result
display_matrix mat_result

echo -e "\n--- MULTIPLICATION ---"
matrix_mul mat_a mat_b mat_result
display_matrix mat_result
```

**Conceptual Q&A:**
**Q: What are associative arrays?**
A: Arrays with string indices (like dictionaries). Declared with `declare -A`.

**Q: Matrix multiplication formula?**
A: C[i][j] = Σ(A[i][k] × B[k][j]) for k=0 to n-1

---

### Q26: Matrix Transpose

**Question:** Write a shell script to find the transpose of a given matrix (interchanging rows and columns).

**Solution:**
```bash
#!/bin/bash

# Read matrix
read_matrix() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    
    echo "Enter matrix ($rows x $cols):"
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            printf "%4d " ${matrix[$i,$j]}
        done
        echo
    done
}

# Transpose matrix
transpose() {
    local rows=$1
    local cols=$2
    local -n original=$3
    local -n transposed=$4
    
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            transposed[$j,$i]=${original[$i,$j]}
        done
    done
}

# Main program
declare -A mat trans

rows=3
cols=3

read_matrix $rows $cols mat

echo -e "\nOriginal Matrix:"
display_matrix $rows $cols mat

transpose $rows $cols mat trans

echo -e "\nTransposed Matrix:"
display_matrix $cols $rows trans
```

**Conceptual Q&A:**
**Q: What is transpose?**
A: Transpose of matrix A is A^T where A^T[i][j] = A[j][i] (swap rows and columns).

**Q: Property of transpose?**
A: (A^T)^T = A, (A+B)^T = A^T + B^T, (AB)^T = B^T × A^T

---

### Q27: Diagonal Sum

**Question:** Write a shell script to find the sum of the main diagonal and secondary diagonal elements of a square matrix.

**Solution:**
```bash
#!/bin/bash

# Read square matrix
read_matrix() {
    local n=$1
    local -n matrix=$2
    
    echo "Enter $n x $n matrix:"
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local n=$1
    local -n matrix=$2
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            printf "%4d " ${matrix[$i,$j]}
        done
        echo
    done
}

# Calculate diagonal sums
diagonal_sum() {
    local n=$1
    local -n matrix=$2
    
    local main_diag=0
    local sec_diag=0
    
    for ((i=0; i<n; i++)); do
        main_diag=$((main_diag + matrix[$i,$i]))
        sec_diag=$((sec_diag + matrix[$i,$((n-1-i))]))
    done
    
    echo "Main diagonal sum: $main_diag"
    echo "Secondary diagonal sum: $sec_diag"
    
    # If odd size matrix, center element counted twice
    if [ $((n % 2)) -eq 1 ]; then
        center=$(( n / 2 ))
        total=$((main_diag + sec_diag - matrix[$center,$center]))
        echo "Total (without double counting center): $total"
    else
        total=$((main_diag + sec_diag))
        echo "Total: $total"
    fi
}

# Main program
declare -A mat

read -p "Enter matrix size: " n
read_matrix $n mat

echo -e "\nMatrix:"
display_matrix $n mat

echo -e "\nDiagonal Sums:"
diagonal_sum $n mat
```

**Conceptual Q&A:**
**Q: What is main diagonal?**
A: Elements where row index equals column index: [0,0], [1,1], [2,2]...

**Q: What is secondary diagonal?**
A: Anti-diagonal from top-right to bottom-left: [0,n-1], [1,n-2], [2,n-3]...

---

### Q28: Check Symmetric Matrix

**Question:** Write a shell script to check whether a given square matrix is symmetric or not (i.e., equal to its transpose).

**Solution:**
```bash
#!/bin/bash

# Read matrix
read_matrix() {
    local n=$1
    local -n matrix=$2
    
    echo "Enter $n x $n matrix:"
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local n=$1
    local -n matrix=$2
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            printf "%4d " ${matrix[$i,$j]}
        done
        echo
    done
}

# Check if symmetric
is_symmetric() {
    local n=$1
    local -n matrix=$2
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            if [ ${matrix[$i,$j]} -ne ${matrix[$j,$i]} ]; then
                return 1  # Not symmetric
            fi
        done
    done
    
    return 0  # Symmetric
}

# Main program
declare -A mat

read -p "Enter matrix size: " n
read_matrix $n mat

echo -e "\nMatrix:"
display_matrix $n mat

if is_symmetric $n mat; then
    echo -e "\nThe matrix is SYMMETRIC"
else
    echo -e "\nThe matrix is NOT SYMMETRIC"
fi
```

**Conceptual Q&A:**
**Q: What is a symmetric matrix?**
A: A matrix equal to its transpose: A = A^T, i.e., A[i][j] = A[j][i] for all i,j.

**Q: Properties of symmetric matrices?**
A: Always square, diagonal elements can be anything, eigenvalues are real.

---

### Q29: Upper and Lower Triangular Matrices

**Question:** Write a shell script to display the upper triangular and lower triangular matrices separately from a given square matrix.

**Solution:**
```bash
#!/bin/bash

# Read matrix
read_matrix() {
    local n=$1
    local -n matrix=$2
    
    echo "Enter $n x $n matrix:"
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local n=$1
    local -n matrix=$2
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            printf "%4d " ${matrix[$i,$j]}
        done
        echo
    done
}

# Extract upper triangular
upper_triangular() {
    local n=$1
    local -n original=$2
    local -n upper=$3
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            if [ $j -ge $i ]; then
                upper[$i,$j]=${original[$i,$j]}
            else
                upper[$i,$j]=0
            fi
        done
    done
}

# Extract lower triangular
lower_triangular() {
    local n=$1
    local -n original=$2
    local -n lower=$3
    
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            if [ $j -le $i ]; then
                lower[$i,$j]=${original[$i,$j]}
            else
                lower[$i,$j]=0
            fi
        done
    done
}

# Main program
declare -A mat upper lower

read -p "Enter matrix size: " n
read_matrix $n mat

echo -e "\nOriginal Matrix:"
display_matrix $n mat

upper_triangular $n mat upper
echo -e "\nUpper Triangular Matrix:"
display_matrix $n upper

lower_triangular $n mat lower
echo -e "\nLower Triangular Matrix:"
display_matrix $n lower
```

**Conceptual Q&A:**
**Q: What is upper triangular matrix?**
A: All elements below main diagonal are zero: A[i][j] = 0 when i > j.

**Q: What is lower triangular matrix?**
A: All elements above main diagonal are zero: A[i][j] = 0 when i < j.

---

### Q30: Search Element in Matrix

**Question:** Write a shell script to search for a specific element in a matrix and display its position (row and column) if found.

**Solution:**
```bash
#!/bin/bash

# Read matrix
read_matrix() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    
    echo "Enter matrix ($rows x $cols):"
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            read -p "Element [$i][$j]: " matrix[$i,$j]
        done
    done
}

# Display matrix
display_matrix() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            printf "%4d " ${matrix[$i,$j]}
        done
        echo
    done
}

# Search element
search_element() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    local target=$4
    local found=0
    
    echo "Searching for $target..."
    
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            if [ ${matrix[$i,$j]} -eq $target ]; then
                echo "Found at position: Row $i, Column $j"
                found=1
            fi
        done
    done
    
    if [ $found -eq 0 ]; then
        echo "Element not found in matrix"
    fi
}

# Main program
declare -A mat

read -p "Enter number of rows: " rows
read -p "Enter number of columns: " cols

read_matrix $rows $cols mat

echo -e "\nMatrix:"
display_matrix $rows $cols mat

read -p "\nEnter element to search: " element
search_element $rows $cols mat $element
```

**Enhanced Version with First Occurrence Only:**
```bash
#!/bin/bash

search_first() {
    local rows=$1
    local cols=$2
    local -n matrix=$3
    local target=$4
    
    for ((i=0; i<rows; i++)); do
        for ((j=0; j<cols; j++)); do
            if [ ${matrix[$i,$j]} -eq $target ]; then
                echo "Found at position: [$i][$j]"
                return 0
            fi
        done
    done
    
    echo "Element not found"
    return 1
}
```

**Conceptual Q&A:**
**Q: How to optimize search in sorted matrix?**
A: Use binary search on rows, then columns. Or start from top-right corner.

**Q: Time complexity of linear search in matrix?**
A: O(m×n) where m=rows, n=columns. Need to check all elements in worst case.

---

## Summary of Key Concepts

### Decision Making
- Use `if-elif-else` for multiple conditions
- Numeric: `-eq, -ne, -gt, -ge, -lt, -le`
- String: `=, !=, -z, -n`
- File: `-e, -f, -d, -r, -w, -x, -s`

### Loops
- **for**: Fixed iterations, ranges, arrays
- **while**: Condition-based, unknown iterations
- **until**: Loop until condition becomes true
- **break**: Exit loop, **continue**: Skip iteration

### Functions
- Define: `function_name() { commands; }`
- Arguments: `$1, $2, ...`, All: `$@`
- Local variables: `local var=value`
- Return: Use `echo` for values, `return` for status

### Arrays
- Indexed: `arr=(1 2 3)`
- Associative: `declare -A arr; arr[key]=value`
- Access: `${arr[index]}`, All: `${arr[@]}`
- Length: `${#arr[@]}`

### String Operations
- Length: `${#str}`
- Substring: `${str:pos:len}`
- Replace: `${str/old/new}`
- Case: `${str^^}` upper, `${str,,}` lower

---
