#!/bin/bash

set -euo pipefail

COMPLETION_DIR="$HOME/.bash_completion.d"
mkdir -p "$COMPLETION_DIR"

cat > "$COMPLETION_DIR/pk" <<'EOF'
#!/bin/bash

_pk_completion() {
    local cur prev opts cmd
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    opts="install remove query rindex up"
    cmd="${COMP_WORDS[1]}"

    if [[ ${COMP_CWORD} -eq 1 ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi

    if [[ ${COMP_CWORD} -gt 1 ]] && { [[ "$cmd" == "install" ]] || [[ "$cmd" == "remove" ]] || [[ "$cmd" == "query" ]]; }; then
        if [[ -n "$cur" ]]; then
            COMPREPLY=( $(xbps-query -l | grep -E "^i.*${cur}" | awk "{print \$2}" | cut -d- -f1) )
        else
            COMPREPLY=( $(xbps-query -l | awk "{print \$2}" | cut -d- -f1) )
        fi
        return 0
    fi

    return 0
}

complete -F _pk_completion pk
EOF

chmod +x "$COMPLETION_DIR/pk"

if ! grep -q "source ~/.bash_completion.d/pk" "$HOME/.bashrc"; then
    echo "" >> "$HOME/.bashrc"
    echo "# Load pk bash completion" >> "$HOME/.bashrc"
    echo "if [ -f \"\$HOME/.bash_completion.d/pk\" ]; then" >> "$HOME/.bashrc"
    echo "    source \"\$HOME/.bash_completion.d/pk\"" >> "$HOME/.bashrc"
    echo "fi" >> "$HOME/.bashrc"
fi

chmod +x "$HOME/.bash_completion.d/pk"
