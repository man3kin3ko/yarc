if [[ -n "${args[--mapfile]}" ]]; then
    mapfile -t DOMAINS < ${args[ips_list]};
    for value in "${DOMAINS[@]}"; do
        grep $value ${args[name_file]};
    done
else
    while IFS= read -r value; do
        grep $value ${args[name_file]};
    done < ${args[ips_list]}
fi