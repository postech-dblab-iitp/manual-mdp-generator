import xml.dom.minidom
import json
import sys

def getMdidString(oid, mdid):
    if type(mdid) is str:
        return str(oid) + '.' + mdid + '.1.0'
    else:
        return str(oid) + '.' + str(mdid) + '.1.0'

class Type:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.isRedistributable = False
        self.isFixedLength = False
        self.passByValue = False
        self.isHashable = False
        self.isMergeJoinable = True
        self.isFixedLength = True
        self.isTextRelated = False
        self.length = '1'
        
        self.equalityOp = ''
        self.inequalityOp = ''
        self.lessThanOp = ''
        self.lessThanEqualsOp = ''
        self.greaterThanOp = ''
        self.greaterThanEqualsOp = ''
        self.comparisonOp = ''
        self.arrayType = ''
        
        self.minAgg = ''
        self.maxAgg = ''
        self.avgAgg = ''
        self.sumAgg = ''
        self.countAgg = ''

    def setAttributes(self, name, mdid, isRedistributable, isFixedLength, passByValue, isHashable):
        self.name = name
        self.mdid = getMdidString(0, mdid)
        self.isRedistributable = isRedistributable
        self.isFixedLength = isFixedLength
        self.passByValue = passByValue
        self.isHashable = isHashable

    def setChildMdids(self, mdid):
        sub_mdid = 0
        self.equalityOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.inequalityOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.lessThanOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.lessThanEqualsOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.greaterThanOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.greaterThanEqualsOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.comparisonOp = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.arrayType = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        
        self.minAgg = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.maxAgg = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.avgAgg = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.sumAgg = getMdidString(0, str(mdid) + '11' + str(sub_mdid))
        sub_mdid = sub_mdid + 1
        self.countAgg = getMdidString(0, str(mdid) + '11' + str(sub_mdid))

    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:Type '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('IsRedistributable=\"' + str(self.isRedistributable).lower() + '\" ')
        serialized_string += ('IsHashable=\"' + str(self.isHashable).lower() + '\" ')
        serialized_string += ('PassByValue=\"' + str(self.passByValue).lower() + '\" ')
        serialized_string += ('IsMergeJoinable=\"' + str(self.isMergeJoinable).lower() + '\" ')
        serialized_string += ('IsFixedLength=\"' + str(self.isFixedLength).lower() + '\" ')
        serialized_string += ('Length=\"' + str(self.length) + '\" ')
        serialized_string += ('IsTextRelated=\"' + str(self.isTextRelated).lower() + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += ('<dxl:EqualityOp Mdid=\"' + self.equalityOp + '\"/>')
        serialized_string += ('<dxl:InequalityOp Mdid=\"' + self.inequalityOp + '\"/>')
        serialized_string += ('<dxl:LessThanOp Mdid=\"' + self.lessThanOp + '\"/>')
        serialized_string += ('<dxl:LessThanEqualsOp Mdid=\"' + self.lessThanEqualsOp + '\"/>')
        serialized_string += ('<dxl:GreaterThanOp Mdid=\"' + self.greaterThanOp + '\"/>')
        serialized_string += ('<dxl:GreaterThanEqualsOp Mdid=\"' + self.greaterThanEqualsOp + '\"/>')
        serialized_string += ('<dxl:ComparisonOp Mdid=\"' + self.comparisonOp + '\"/>')
        serialized_string += ('<dxl:ArrayType Mdid=\"' + self.arrayType + '\"/>')
        serialized_string += ('<dxl:MinAgg Mdid=\"' + self.minAgg + '\"/>')
        serialized_string += ('<dxl:MaxAgg Mdid=\"' + self.maxAgg + '\"/>')
        serialized_string += ('<dxl:AvgAgg Mdid=\"' + self.avgAgg + '\"/>')
        serialized_string += ('<dxl:SumAgg Mdid=\"' + self.sumAgg + '\"/>')
        serialized_string += ('<dxl:CountAgg Mdid=\"' + self.countAgg + '\"/>')
        
        # Print ending
        serialized_string += '</dxl:Type>'
        
        return serialized_string
    
    
class GPDBScalaOp:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.comparisionType = ''
        self.returnsNullOnNullInput = True
        self.isNDVPreserving = False
        
        self.leftType = ''
        self.rightType = ''
        self.resultType = ''
        self.opFunc = ''
        self.commutator = ''
        self.inverseOp = ''
    
    def setAttributes(self, name, mdid, comparisionType, leftType, rightType, resultType, commutator, inverseOp):
        self.name = name
        self.mdid = mdid
        self.comparisionType = comparisionType
        self.leftType = leftType
        self.rightType = rightType
        self.resultType = resultType
        self.opFunc = mdid + '.' + '0'
        self.commutator = commutator
        self.inverseOp = inverseOp
    
    def getOid():
        return str(0)
    
    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:GPDBScalarOp '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('ComparisonType=\"' + self.comparisionType + '\" ')
        serialized_string += ('ReturnsNullOnNullInput=\"' + str(self.returnsNullOnNullInput).lower() + '\" ')
        serialized_string += ('IsNDVPreserving=\"' + str(self.isNDVPreserving).lower() + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += ('<dxl:LeftType Mdid=\"' + self.leftType + '\"/>')
        serialized_string += ('<dxl:RightType Mdid=\"' + self.rightType + '\"/>')
        #serialized_string += ('<dxl:ResultType Mdid=\"' + self.resultType + '\"/>')
        serialized_string += ('<dxl:OpFunc Mdid=\"' + self.opFunc + '\"/>')
        serialized_string += ('<dxl:Commutator Mdid=\"' + self.commutator + '\"/>')
        serialized_string += ('<dxl:InverseOp Mdid=\"' + self.inverseOp + '\"/>')
        serialized_string += ('<dxl:Opfamilies/>')
        
        # Print ending
        serialized_string += '</dxl:GPDBScalarOp>'
        
        return serialized_string
    
class GPDBAgg:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        
        self.resultType = ''
        self.intermediateResultType = ''
    
    def getOid():
        return str(0)    

    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:GPDBAgg '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += ('<dxl:ResultType Mdid=\"' + self.resultType + '\"/>')
        serialized_string += ('<dxl:IntermediateResultType Mdid=\"' + self.intermediateResultType + '\"/>')
        
        # Print ending
        serialized_string += '</dxl:GPDBAgg>'
        
        return serialized_string
    
class Relation:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.isTemporary = False
        self.storageType = 'Heap'
        self.distributionPolicy = 'MasterOnly'
        
        self.columns = []
        self.indexInfoList = []
        
        self.maxColumns = 0
    
    def setAttributes(self, name, mdid, isTemporary):
        self.name = name
        self.mdid = getMdidString(6, mdid)
        self.isTemporary = isTemporary
    
    def setColumns(self, columns_json):
        column_counter = 1
        for column_json in columns_json:
            # Create column instance
            column = Column()
            
            # Get attributes
            name = column_json['Name']
            mdid = self.mdid.split('.')[1]
            attno = column_counter
            nullable = column_json['Nullable']
            
            # Set attributes
            column.setAttributes(name, mdid, attno, nullable)
            
            # Update counter
            column_counter = column_counter + 1
            
            # Append
            self.columns.append(column)
        
        # Set max column count
        self.maxColumns = column_counter - 1
        
        # Create default columns
        additional_column_names = ['ctid', 'tableoid', 'gp_segment_id'] 
        additional_column_attnos = [-1, -7, -8]
        
        for column_name, column_attno in zip(additional_column_names, additional_column_attnos):
            # Create column instance
            column = Column()
            
            # Get attributes
            mdid = self.mdid.split('.')[1]
            nullable = False
            
            # Set attributes
            column.setAttributes(column_name, mdid, column_attno, nullable)
            
            # Update counter
            column_counter = column_counter + 1
            
            # Append
            self.columns.append(column)
            
    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:Relation '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('IsTemporary=\"' + str(self.isTemporary).lower() + '\" ')
        serialized_string += ('StorageType=\"' + self.storageType + '\" ')
        serialized_string += ('DistributionPolicy=\"' + self.distributionPolicy + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += '<dxl:Columns>'
        for column in self.columns:
            serialized_string += column.serialize()
        serialized_string += '</dxl:Columns>'
        if len(self.indexInfoList) == 0:
            serialized_string += ('<dxl:IndexInfoList/>')
        else:
            serialized_string += '<dxl:IndexInfoList>'
            for indexInfo in self.indexInfoList:
                serialized_string += ('<dxl:IndexInfo Mdid=\"' + indexInfo.mdid + '\"' + ' IsPartial=\"false\"' + '/>')
            serialized_string += '</dxl:IndexInfoList>'
        serialized_string += ('<dxl:Triggers/>')
        serialized_string += ('<dxl:CheckConstraints/>')
        
        # Print ending
        serialized_string += '</dxl:Relation>'
        
        return serialized_string
    
class Column:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.attno = 0
        self.nullable = False
    
    def setAttributes(self, name, mdid, attno, nullable):
        self.name = name
        self.mdid = getMdidString(0, mdid)
        self.attno = attno
        self.nullable = nullable
    
    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:Column '
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('Attno=\"' + str(self.attno) + '\" ')
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Nullable=\"' + str(self.nullable).lower() + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += ('<dxl:DefaultValue/>')
        
        # Print ending
        serialized_string += '</dxl:Column>'
        
        return serialized_string
    
class Index:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.relationMdid = ''
        self.isClustered = False
        self.keyColumns = []
        self.includedColumns = []
        
    def setAttributes(self, name, mdid, relationMdid, isClustered, keyColumns, includedColumns):
        self.name = name
        self.mdid = getMdidString(7, mdid)
        self.relationMdid = relationMdid
        self.isClustered = isClustered
        self.keyColumns = keyColumns
        self.includedColumns = includedColumns

    def getOid():
        return str(7)    

    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:Index '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('RelationMdid=\"' + self.relationMdid + '\" ')
        serialized_string += ('IsClustered=\"' + str(self.isClustered).lower() + '\" ')
        serialized_string += ('KeyColumns=\"' + ','.join(self.keyColumns) + '\" ')
        serialized_string += ('IncludedColumns=\"' + ','.join(self.includedColumns) + '\" ')
        serialized_string += '>'
        
        # Print childs
        serialized_string += ('<dxl:Opfamiles/>')
        
        # Print ending
        serialized_string += '</dxl:Index>'
        
        return serialized_string
    
class RelationStatistics:
    def __init__(self) -> None:
        self.name = ''
        self.mdid = ''
        self.rows = 0
        
    def setAttributes(self, name, mdid, rows):
        self.name = name
        self.mdid = getMdidString(2, mdid)
        self.rows = rows
    
    def getOid():
        return str(1)    
        
    def serialize(self) -> str:
        # Print attributes
        serialized_string = '<dxl:RelationStatistics '
        serialized_string += ('Mdid=\"' + self.mdid + '\" ')
        serialized_string += ('Name=\"' + self.name + '\" ')
        serialized_string += ('Rows=\"' + str(self.rows) + '\" ')
        serialized_string += '/>'
        
        return serialized_string
    
type_list = []
scala_op_list = []
agg_list = []
relation_list = []
index_list = []
relation_statistics_list = []

json_file_path = sys.argv[1]
mdid_clock = 1
bool_mdid = ''

with open(json_file_path, 'r') as json_file:
    spec_json = json.load(json_file)
    
    # Type instance generation and mdid assignment
    # Get type list
    type_json_list = spec_json['Types']
    for type_json in type_json_list:
        # Create type instance
        new_type = Type()
        
        # Get instance attributes
        name = type_json['Name']
        isRedistributable = (type_json['IsRedistributable'] if 'IsRedistributable' in type_json else True)
        isFixedLength = (type_json['IsFixedLength'] if 'IsFixedLength' in type_json else False)
        passByValue = (type_json['PassByValue'] if 'PassByValue' in type_json else False)
        isHashable = (type_json['IsHashable'] if 'IsHashable' in type_json else False)
        
        # Mdid gen
        mdid = mdid_clock
        mdid_clock = mdid_clock + 1
        
        # Set attributes
        new_type.setAttributes(name, mdid, isRedistributable, isFixedLength, passByValue, isHashable)
        
        # Set child mdids
        new_type.setChildMdids(mdid)
        
        # Append to list
        type_list.append(new_type)
        
        # If boolean, store its mdid
        if name == 'bool':
            bool_mdid = new_type.mdid
    
    # GPDBScalaOp and GPDBAgg instance generation and mdid assignment
    for type_instance in type_list:
        type_mdid = type_instance.mdid
        
        # GPDBScalaOp
        equality_mdid = type_instance.equalityOp
        inequality_mdid = type_instance.inequalityOp
        less_than_mdid = type_instance.lessThanOp
        less_than_equal_mdid = type_instance.lessThanEqualsOp
        greater_than_mdid = type_instance.greaterThanOp
        greater_than_equal_mdid = type_instance.greaterThanEqualsOp
        comparison_mdid = type_instance.comparisonOp
        
        # Equality
        equality_op = GPDBScalaOp()
        equality_op.setAttributes('=', equality_mdid, 'Eq', type_mdid, type_mdid, bool_mdid, equality_mdid, inequality_mdid)
        scala_op_list.append(equality_op)
        
        # Inequality
        inequality_op = GPDBScalaOp()
        inequality_op.setAttributes('!=', inequality_mdid, 'NEq', type_mdid, type_mdid, bool_mdid, inequality_mdid, equality_mdid)
        scala_op_list.append(inequality_op)
        
        # Lessthan
        less_than_op = GPDBScalaOp()
        less_than_op.setAttributes('lt', less_than_mdid, 'LT', type_mdid, type_mdid, bool_mdid, greater_than_mdid, greater_than_equal_mdid)
        scala_op_list.append(less_than_op)
        
        # Lessthanequal
        less_than_equal_op = GPDBScalaOp()
        less_than_equal_op.setAttributes('leq', less_than_equal_mdid, 'LEq', type_mdid, type_mdid, bool_mdid, greater_than_equal_mdid, greater_than_mdid)
        scala_op_list.append(less_than_equal_op)
        
        # Greaterthan
        greater_than_op = GPDBScalaOp()
        greater_than_op.setAttributes('gt', greater_than_mdid, 'GT', type_mdid, type_mdid, bool_mdid, less_than_mdid, less_than_equal_mdid)
        scala_op_list.append(greater_than_op)
        
        # Greaterthanequal
        greater_than_equal_op = GPDBScalaOp()
        greater_than_equal_op.setAttributes('geq', greater_than_equal_mdid, 'GEq', type_mdid, type_mdid, bool_mdid, less_than_equal_mdid, less_than_mdid)
        scala_op_list.append(greater_than_equal_op)
        
        # GPDBAggOp
        min_agg_mid = type_instance.minAgg
        max_agg_mid = type_instance.maxAgg
        avg_agg_mid = type_instance.avgAgg
        sum_agg_mid = type_instance.sumAgg
        count_agg_mid = type_instance.countAgg
        
    # Relation instance generation and mdid assignment
    # Get relation list
    relation_json_list = spec_json['Relations']
    for relation_json in relation_json_list:
        # Create relation instance
        new_relation = Relation()
        
        # Mdid gen
        mdid = mdid_clock
        mdid_clock = mdid_clock + 1
        
        # Get attributes
        name = relation_json['Name']
        isTemporary = False
        
        # Set attributes
        new_relation.setAttributes(name, str(mdid), isTemporary)
        
        # Set columns
        new_relation.setColumns(relation_json['Columns'])
        
        # Append relation
        relation_list.append(new_relation)
        
    # Index instance generation and mdid assignment
    # Get index list
    index_json_list = spec_json['Indicies']
    for index_json in index_json_list:
        # Create index instance
        new_index = Index()
        
        # Mdid gen
        mdid = mdid_clock
        mdid_clock = mdid_clock + 1
        
        # Get attributes
        name = index_json['Name']
        relation_name = index_json['Relation']
        is_clustered = index_json['Is_clustered']
        key_column_names = index_json['Key_columns']
        
        # Convert attributes
        relation = None
        relation_mdid = ''
        key_columns = []
        included_columns = []
        
        for relation in relation_list:
            # Get relation
            if relation.name == relation_name: 
                # Get relation mdid
                relation_mdid = relation.mdid
                # Get columns
                for column in relation.columns:
                    if column.name in key_column_names:
                        key_columns.append(str(int(column.attno) - 1))
                # Generate included columns
                for i in range(0, relation.maxColumns):
                    included_columns.append(str(i))
                # Assign indexInfoList
                relation.indexInfoList.append(new_index)
                # Break the loop
                break
        
        # Set attributes
        new_index.setAttributes(name, str(mdid), relation_mdid, is_clustered, key_columns, included_columns)
        
        # Append
        index_list.append(new_index)
        
    # RelationStatistics instance generation and mdid assignment
    # Get relation statistics list
    relation_statistics_json_list = spec_json['Relation_statistics']
    for relation_statistics_json in relation_statistics_json_list:
        # Create RS instance
        new_relation_statistics = RelationStatistics()
        
        # Get attributes
        relation_name = relation_statistics_json['Relation']
        rows = relation_statistics_json['Rows']
        
        # Get relation mdid
        relation_mdid = ''
        for relation in relation_list:
            if relation.name == relation_name: 
                relation_mdid = relation.mdid
                
        # Generate mdid
        mdid = mdid_clock
        mdid_clock = mdid_clock + 1
        
        # Set attributes
        new_relation_statistics.setAttributes(name, str(mdid), rows)
        
        # Append
        relation_statistics_list.append(new_relation_statistics)
        
# Print
mdp_string = '<?xml version="1.0" encoding="UTF-8"?>'
mdp_string += '<dxl:DXLMessage xmlns:dxl="http://greenplum.com/dxl/2010/12/">'
mdp_string += '<dxl:Thread Id="0">'
mdp_string += '<dxl:Metadata SystemIds="0.GPDB">'

# Type print
for type_instance in type_list:
    mdp_string += type_instance.serialize()

# GPDBScalaOp print
for scala_op in scala_op_list:
    mdp_string += scala_op.serialize()

# GPDBAgg print
for agg in agg_list:
    mdp_string += agg.serialize()

# Relation print
for relation in relation_list:
    mdp_string += relation.serialize()

# Index print
for index in index_list:
    mdp_string += index.serialize()

# RelationStatistics print
for relation_statistics in relation_statistics_list:
    mdp_string += relation_statistics.serialize()

mdp_string += '</dxl:Metadata>'
mdp_string += '</dxl:Thread>'
mdp_string += '</dxl:DXLMessage>'

# Write to file
with open('raw_mdp.mdp', 'w') as raw_mdp:
    raw_mdp.write(mdp_string)
    
# Pretty print to file
dom = xml.dom.minidom.parse('raw_mdp.mdp')
pretty_mdp_as_string = dom.toprettyxml()

with open('pretty_mdp.mdp', 'w') as pretty_mdp:
    pretty_mdp.write(pretty_mdp_as_string)
    
    
# Dump relation mdids
relation_mdid_dict = {}
for relation in relation_list:
    relation_mdid_dict[relation.name] = relation.mdid

with open('relation_mdid.txt', 'w') as relation_mdid_file:
    relation_mdid_file.write(json.dumps(relation_mdid_dict))