import collections
import os
import pytest

from tandemrepeats.repeat_list import repeat_list as rl
from tandemrepeats.repeat import repeat
from tandemrepeats.repeat_list import repeat_list_io as rl_io

TEST_REPEATS = [["AA","AA"],["AAA","AAA"]]
TEST_SEQUENCE = "JAAAAKAAAAAAL"
TEST_SCORE = "phylo_gap01"
TEST_SCORE_VALUE_LIST = [0.0, 0.5]
TEST_BEGIN_LIST = [6,10]
TEST_TSV = "msa_original\tbegin\tnD\tlD\tsequence_length\tpValue\nAA,AA\t2\t2.0\t2\t4\tNone\nAAA,AAA\t7\t2.0\t3\t6\tNone"


def test_serialize_repeat_list_tsv():

    test_repeats = [repeat.Repeat(msa = i) for i in TEST_REPEATS]
    for i in test_repeats:
        i.repeat_in_sequence(sequence = TEST_SEQUENCE)
    test_repeat_list = rl.Repeat_list(repeats = test_repeats)

    tsv = rl_io.serialize_repeat_list_tsv(test_repeat_list)

    assert tsv == TEST_TSV
