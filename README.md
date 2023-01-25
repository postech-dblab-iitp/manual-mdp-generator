# Synthetic GDB MDP Generator

## Usage

```
./generator.py <configuration file>
```

## Output
```
raw_mdp.mdp: raw mdp file
pretty_mdp.mdp: pretty print mdp file
relation_mdid.txt: relation mdid mapping
```

## MDID rule

- Relation
    - 6.rand_num.1.0
- Column
    - 0.'relaion_mdid'.concat('0' + 'rand_num').1.0
- Index
    - 7.rand_num.1.0
- Type
    - 0.rand_num.1.0
- GPDBAgg
    - 0.'type_mdid'.concat('00' + 'rand_num').1.0
- GPDBScalaOp
    - 0.'type_mdid'.concat('00' + 'rand_num').1.0
- RelationStatistics
    - 2.rand_num.1.0
