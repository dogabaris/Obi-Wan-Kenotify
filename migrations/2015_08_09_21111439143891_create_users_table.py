from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username', 30).unique()
            table.string('password', 30)

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
