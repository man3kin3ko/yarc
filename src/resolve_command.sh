if [[ -n "${args[--mapfile]}" ]]; then
    mapfile -t DOMAINS < ${args[hostnames_list]};
    for value in "${DOMAINS[@]}"; do
        dig +noall +answer $value | awk '{print $5}' | xargs -L1 echo "$value";
    done
else
    while IFS= read -r value; do
        dig +noall +answer $value | awk '{print $5}' | xargs -L1 echo "$value";
    done < ${args[hostnames_list]}
fi