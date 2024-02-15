<template>
    <div>
        <v-file-input
            v-model="file"
            accept="image/*"
            label="Select an image"
            @change="onFileChange"
        ></v-file-input>
    </div>
</template>