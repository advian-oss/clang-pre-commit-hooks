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
        for arg in checker.args:
            assert not arg.startswith("-DCMAKE_EXPORT_COMPILE_COMMANDS")

    @staticmethod
    def test_clang_tidy_dash_notpresent(klass) -> None:
        """If -p is *not* in arguments make sure -DCMAKE_EXPORT_COMPILE_COMMANDS is defined"""
        checker = klass([])
        export_found = False
        for arg in checker.args:
            if arg.startswith("-DCMAKE_EXPORT_COMPILE_COMMANDS"):
                export_found = True
                break
        assert export_found
