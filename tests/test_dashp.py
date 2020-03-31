"""Test oclint and clang-tidy -p argument"""
from hooks.clang_tidy import ClangTidyCmd
from hooks.oclint import OCLintCmd


class TestHDashp:
    """Deal with the conftest weirdness"""

    @classmethod
    def setup_class(cls):
        """Setup the scenario list"""
        cls.scenarios = [
            ["ClangTidyCmd", {"klass": ClangTidyCmd}],
            ["OCLintCmd", {"klass": OCLintCmd}],
        ]

    @staticmethod
    def test_clang_tidy_dashp_present(klass) -> None:
        """If -p is in arguments make sure -DCMAKE_EXPORT_COMPILE_COMMANDS is *not*"""
        checker = klass(["-p=cmake-build-debug"])
        dashp_found = False
        for arg in checker.args:
            assert not arg.startswith("-DCMAKE_EXPORT_COMPILE_COMMANDS")
            if arg.startswith("-p"):
                dashp_found = True
        assert dashp_found

    @staticmethod
    def test_clang_tidy_dashp_notpresent(klass) -> None:
        """Test missing -p, make sure the flag isn't there in that case either"""
        checker = klass([])
        for arg in checker.args:
            assert not arg.startswith("-DCMAKE_EXPORT_COMPILE_COMMANDS")
            assert not arg.startswith("-p")
