#!/usr/bin/env bash
set -e

if ! command -v ufosay &> /dev/null; then
    echo "Installing ufosay via pip..."
    pip install .
fi

SHELL_CONFIG=""
if [ -n "$BASH" ] && [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ] && [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
fi

ALIASES=$(cat << 'EOF'

# ufosay - mistype triggers for ls
alias ks='ufosay "Did you mean ls?"'
alias cl='ufosay "Did you mean ls?"'
alias xl='ufosay "Did you mean ls?"'
alias lw='ufosay "Did you mean ls?"'
alias lz='ufosay "Did you mean ls?"'
EOF
)

if grep -q "ufosay" "$SHELL_CONFIG" 2>/dev/null; then
    echo "ufosay aliases already present in $SHELL_CONFIG"
else
    echo "$ALIASES" >> "$SHELL_CONFIG"
    echo "Added ufosay aliases to $SHELL_CONFIG"
fi

echo ""
echo "ufosay installed! Restart your terminal or run:"
echo "  source $SHELL_CONFIG"
echo ""
echo "Try: ufosay 'Hello from space!'"
