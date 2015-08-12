from orator.migrations import Migration


class CreateTagsUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tags_users') as table:
            table.integer('tag_id')
            table.integer('user_id')

            table.foreign('user_id').references('id').on('users')
            table.foreign('tag_id').references('id').on('tags')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tags_users')
